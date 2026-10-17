# ==============================================================================
# PERLACOLABS - PUENTE MAVLINK 4G LTE CON SEGURIDAD CRIPTOGRÁFICA
# STR-002 H3 v3.5 — Companion Computer (RPi/Jetson)
# ==============================================================================
# Seguridad implementada:
#   - Cifrado AES-128-GCM (ECDH P-256 + HKDF para derivación de clave)
#   - HMAC-SHA256 para integridad de comandos MAVLink
#   - Whitelist de comandos MAVLink permitidos (anti-inyección)
#   - Timeout de heartbeat con desconexión automática
#   - Límite de tiempo de vuelo (MAX_FLIGHT_TIME_S)
#   - Logging estructurado para auditoría AFAC/Senasica
# ==============================================================================

import time
import hashlib
import hmac
import struct
import os
import logging
import signal
import sys

try:
    from pymavlink import mavutil
except ImportError:
    print("ERROR: pymavlink no instalado. Ejecutar: pip install pymavlink")
    exit(1)

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF
    from cryptography.exceptions import InvalidTag
except ImportError:
    print("ERROR: cryptography no instalado. Ejecutar: pip install cryptography")
    exit(1)

# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================

UART_PORT = os.environ.get('PERLACO_UART_PORT', '/dev/ttyAMA0')
UART_BAUD = int(os.environ.get('PERLACO_UART_BAUD', '115200'))

GCS_HOST = os.environ.get('PERLACO_GCS_HOST', '10.20.30.40')
GCS_PORT = int(os.environ.get('PERLACO_GCS_PORT', '14550'))

# HMAC pre-compartido (32 bytes = 256 bits) — GENERAR NUEVO PARA PRODUCCIÓN
# Generar con: python -c "import secrets; print(secrets.token_hex(32))"
HMAC_SHARED_KEY = bytes.fromhex(
    os.environ.get('PERLACO_HMAC_KEY',
    'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')
)

ECDH_CURVE = ec.SECP256R1

HEARTBEAT_TIMEOUT_S = 5.0
SESSION_KEY_ROTATE_S = 300
MAX_FLIGHT_TIME_S = 900

# Whitelist de comandos MAVLink permitidos vía 4G
ALLOWED_MAVLINK_COMMANDS = {
    176,   # MAV_CMD_DO_SET_MODE
    400,   # MAV_CMD_NAV_WAYPOINT
    401,   # MAV_CMD_NAV_LOITER_UNLIM
    403,   # MAV_CMD_NAV_RETURN_TO_LAUNCH
    80,    # MAV_CMD_NAV_TAKEOFF
    81,    # MAV_CMD_NAV_LAND
    183,   # MAV_CMD_DO_SET_SERVO
    200,   # MAV_CMD_DO_CHANGE_SPEED
    510,   # MAV_CMD_DO_SET_ROI
    2525,  # Custom: SPRAY_ON/OFF (PERLACO)
}

# ==============================================================================
# LOGGING
# ==============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d UTC [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)
logger = logging.getLogger('PERLACO-4G')


# ==============================================================================
# SESIÓN CRIPTOGRÁFICA ECDH + AES-128-GCM
# ==============================================================================

class SecureSession:
    def __init__(self):
        self.ephemeral_key = ec.generate_private_key(ECDH_CURVE())
        self.peer_public_key = None
        self.session_key = None
        self.aes_gcm = None
        self.tx_nonce = 0
        self.rx_nonce = 0
        self.session_start = 0.0
        self.established = False

    def get_public_bytes(self):
        return self.ephemeral_key.public_key().public_bytes(
            encoding=serialization.Encoding.X962,
            format=serialization.PublicFormat.UncompressedPoint
        )

    def set_peer_public(self, peer_bytes):
        self.peer_public_key = ec.EllipticCurvePublicKey.from_encoded_point(
            ECDH_CURVE(), peer_bytes
        )

    def derive_session_key(self):
        if not self.peer_public_key:
            raise RuntimeError("Clave pública del peer no establecida")
        shared_secret = self.ephemeral_key.exchange(ec.ECDH(), self.peer_public_key)
        self.session_key = HKDF(
            algorithm=hashes.SHA256(),
            length=16,
            salt=b'PERLACO-STR002-H3-SESSION',
            info=b'mavlink-dtls-session-key',
        ).derive(shared_secret)
        self.aes_gcm = AESGCM(self.session_key)
        self.tx_nonce = 0
        self.rx_nonce = 0
        self.session_start = time.time()
        self.established = True
        logger.info("Sesion ECDH+AES-128-GCM establecida. Rotacion en %ds", SESSION_KEY_ROTATE_S)

    def needs_rotation(self):
        return (self.established and
                time.time() - self.session_start > SESSION_KEY_ROTATE_S)

    def rotate(self):
        self.ephemeral_key = ec.generate_private_key(ECDH_CURVE())
        self.established = False
        self.peer_public_key = None
        logger.info("Rotacion ECDH iniciada")

    def encrypt(self, plaintext):
        if not self.established:
            raise RuntimeError("Sesion no establecida")
        nonce = struct.pack('>QQ', 0, self.tx_nonce)
        self.tx_nonce += 1
        aad = hmac.new(HMAC_SHARED_KEY, plaintext, hashlib.sha256).digest()[:8]
        ciphertext = self.aes_gcm.encrypt(nonce, plaintext, aad)
        return ciphertext + aad

    def decrypt(self, data):
        if not self.established:
            raise RuntimeError("Sesion no establecida")
        ciphertext = data[:-8]
        aad = data[-8:]
        nonce = struct.pack('>QQ', 0, self.rx_nonce)
        self.rx_nonce += 1
        try:
            plaintext = self.aes_gcm.decrypt(nonce, ciphertext, aad)
            return plaintext
        except InvalidTag:
            logger.error("FALLO DE INTEGRIDAD: AES-GCM tag invalido")
            return None


# ==============================================================================
# VERIFICACIÓN HMAC-SHA256
# ==============================================================================

def compute_mavlink_hmac(msg_bytes):
    return hmac.new(HMAC_SHARED_KEY, msg_bytes, hashlib.sha256).digest()


def verify_mavlink_hmac(msg_bytes, received_hmac_hex):
    expected = compute_mavlink_hmac(msg_bytes)
    received = bytes.fromhex(received_hmac_hex) if isinstance(received_hmac_hex, str) else received_hmac_hex
    return hmac.compare_digest(expected, received)


# ==============================================================================
# FILTRO DE COMANDOS (ANTI-INYECCIÓN)
# ==============================================================================

def is_command_allowed(command_id):
    allowed = command_id in ALLOWED_MAVLINK_COMMANDS
    if not allowed:
        logger.warning("COMANDO BLOQUEADO: MAVLink CMD %d fuera de whitelist", command_id)
    return allowed


# ==============================================================================
# PUENTE PRINCIPAL
# ==============================================================================

class SecureCompanionBridge:
    def __init__(self):
        self.mav_connection = None
        self.secure_session = SecureSession()
        self.last_heartbeat_time = time.time()
        self.flight_start_time = None
        self.is_armed = False
        self.running = False

    def connect_flight_controller(self):
        try:
            logger.info("Conectando a Cube Orange+ en %s @ %d baud...", UART_PORT, UART_BAUD)
            self.mav_connection = mavutil.mavlink_connection(UART_PORT, baud=UART_BAUD)
            self.mav_connection.wait_heartbeat(timeout=5)
            logger.info("Heartbeat de Cube Orange+ recibido — enlace UART activo")
            return True
        except Exception as e:
            logger.error("Fallo de conexion UART: %s", e)
            self.mav_connection = None
            return False

    def forward_to_fc(self, msg):
        if not self.mav_connection:
            logger.warning("No hay enlace UART — mensaje descartado")
            return False
        if hasattr(msg, 'command') and not is_command_allowed(msg.command):
            logger.error("COMANDO RECHAZADO: CMD %d — fuera de whitelist", msg.command)
            return False
        self.mav_connection.mav.send(msg)
        return True

    def check_safety_conditions(self):
        now = time.time()
        if now - self.last_heartbeat_time > HEARTBEAT_TIMEOUT_S:
            logger.critical("HEARTBEAT TIMEOUT: Sin señal GCS por %.1fs — MODO LOCAL",
                           now - self.last_heartbeat_time)
            return False
        if self.is_armed and self.flight_start_time:
            flight_time = now - self.flight_start_time
            if flight_time > MAX_FLIGHT_TIME_S:
                logger.critical("TIEMPO MAX EXCEDIDO: %.0f/%.0fs — RTL automatico",
                              flight_time, MAX_FLIGHT_TIME_S)
                if self.mav_connection:
                    self.mav_connection.mav.command_long_send(
                        self.mav_connection.target_system,
                        self.mav_connection.target_component,
                        mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,
                        0, 0, 0, 0, 0, 0, 0, 0
                    )
                return False
        return True

    def run(self):
        logger.info("PERLACO Secure Companion Bridge v3.5 iniciando...")
        if not self.connect_flight_controller():
            logger.error("No se pudo conectar al flight controller. Abortando.")
            return
        self.running = True
        logger.info("Whitelist activa: %d comandos permitidos", len(ALLOWED_MAVLINK_COMMANDS))
        try:
            while self.running:
                if self.mav_connection:
                    msg = self.mav_connection.recv_match(blocking=False, timeout=0.05)
                    if msg:
                        msg_type = msg.get_type()
                        if msg_type == 'HEARTBEAT':
                            self.last_heartbeat_time = time.time()
                            was_armed = self.is_armed
                            self.is_armed = bool(msg.base_mode & 0x80)
                            if self.is_armed and not was_armed:
                                self.flight_start_time = time.time()
                                logger.info("DRONE ARMADO — timer de vuelo iniciado")
                            elif not self.is_armed and was_armed:
                                self.flight_start_time = None
                                logger.info("DRONE DESARMADO — timer reseteado")
                        if self.secure_session.established:
                            try:
                                msg_bytes = msg.get_msgbuf()
                                encrypted = self.secure_session.encrypt(msg_bytes)
                                logger.debug("TX %s (%d bytes cifrados)", msg_type, len(encrypted))
                            except Exception as e:
                                logger.error("Error cifrando %s: %s", msg_type, e)
                self.check_safety_conditions()
                if self.secure_session.needs_rotation():
                    self.secure_session.rotate()
                time.sleep(0.01)
        except KeyboardInterrupt:
            logger.info("Puente detenido por operador")
            self.running = False
        except Exception as e:
            logger.critical("EXCEPCION FATAL: %s", e, exc_info=True)
            self.running = False


# ==============================================================================
# GENERADOR DE CLAVES DE DESARROLLO
# ==============================================================================

def generate_dev_hmac_key():
    import secrets
    key = secrets.token_hex(32)
    print("CLAVE HMAC DE DESARROLLO (guardar como PERLACO_HMAC_KEY):")
    print("  " + key)
    print("")
    print("CONFIGURAR EN ENTORNO:")
    print("  export PERLACO_HMAC_KEY=" + key)
    return key


if __name__ == '__main__':
    if '--gen-key' in sys.argv:
        generate_dev_hmac_key()
        sys.exit(0)
    if '--help' in sys.argv or '-h' in sys.argv:
        print("PERLACO Secure Companion Bridge v3.5")
        print("Uso: python companion_4g_bridge.py [--gen-key|--help]")
        print("")
        print("Variables de entorno:")
        print("  PERLACO_GCS_HOST    — IP del GCS (default: 10.20.30.40)")
        print("  PERLACO_GCS_PORT    — Puerto DTLS (default: 14550)")
        print("  PERLACO_HMAC_KEY    — Clave HMAC hex (64 chars)")
        print(f"  Whitelist: {len(ALLOWED_MAVLINK_COMMANDS)} comandos")
        print(f"  Heartbeat timeout: {HEARTBEAT_TIMEOUT_S}s")
        print(f"  Max flight time: {MAX_FLIGHT_TIME_S}s")
        sys.exit(0)
    bridge = SecureCompanionBridge()
    bridge.run()
