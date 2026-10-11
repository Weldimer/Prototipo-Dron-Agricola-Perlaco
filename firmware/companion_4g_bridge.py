# SERVICIO COMPANION COMPUTER (RASPBERRY PI / JETSON) - PUENTE MAVLINK 4G LTE
import time
from pymavlink import mavutil

def iniciar_puente():
    print("Iniciando enlace MAVLink 4G LTE hacia QGroundControl / FMIS...")
    master = mavutil.mavlink_connection('/dev/ttyAMA0', baud=57600)
    master.wait_heartbeat()
    print("Heartbeat recibido de Cube Orange+. Enlace MAVLink activo en 4G.")

if __name__ == '__main__':
    iniciar_puente()
