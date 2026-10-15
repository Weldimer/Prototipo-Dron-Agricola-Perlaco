import time
import json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class SecureTelemetryBridge:
    def __init__(self, master_key_hex=None):
        if master_key_hex:
            self.key = bytes.fromhex(master_key_hex)
        else:
            self.key = AESGCM.generate_key(bit_length=256)
        self.aesgcm = AESGCM(self.key)
        self.last_nonce_counter = 0

    def cifrar_paquete(self, datos_dict):
        self.last_nonce_counter += 1
        timestamp_bytes = int(time.time() * 1000).to_bytes(4, 'big')
        counter_bytes = self.last_nonce_counter.to_bytes(8, 'big')
        nonce = counter_bytes + timestamp_bytes
        payload_bytes = json.dumps(datos_dict).encode('utf-8')
        associated_data = b"STR-002-H3-SECURE-MESH"
        ciphertext = self.aesgcm.encrypt(nonce, payload_bytes, associated_data)
        return {'nonce': nonce.hex(), 'payload': ciphertext.hex()}

    def descifrar_paquete(self, paquete_seguro):
        try:
            nonce = bytes.fromhex(paquete_seguro['nonce'])
            ciphertext = bytes.fromhex(paquete_seguro['payload'])
            associated_data = b"STR-002-H3-SECURE-MESH"
            decrypted_bytes = self.aesgcm.decrypt(nonce, ciphertext, associated_data)
            return json.loads(decrypted_bytes.decode('utf-8'))
        except Exception as e:
            print(f"❌ [Error de Seguridad] Integridad violada: {e}")
            return None
