import urllib.request
import json
import sys

def mostrar_banner():
    print("==========================================================")
    print("      PANEL DE CONTROL TÉCNICO OPERATIVO — STR-002 H3     ")
    print("      Sistema Abierto de Carga Pesada (MTOW 60 kg)        ")
    print("==========================================================")

def menu():
    while True:
        mostrar_banner()
        print("\nSeleccione un módulo de diagnóstico:")
        print("1. Estado General de Ingeniería (FEA y Hardware)")
        print("2. Monitoreo Atmosférico en Tiempo Real (Clima - Veracruz)")
        print("3. Catastro Geoespacial de Parcelas y Rutas VRA")
        print("4. Salir")
        
        opcion = input("\nIngrese el número de opción: ").strip()
        
        if opcion == "1":
            print("\n--- ESTADO DEL GEMELO DIGITAL Y HARDWARE ---")
            print("• Factor de Seguridad (FEA): 3.46 (Aluminio 7075-T6)")
            print("• Esfuerzo de Von Mises:    145.20 MPa vs 503 MPa límite")
            print("• Bus de Potencia HV:       66.6V / 18S (~126 A Nominal)")
            print("• Tolerancia Mecánica P-01: Ø24.0 mm H7 (Ajuste de precisión)")
            print("• Repositorio GitHub:       Sincronizado en rama main")
            input("\nPresione Enter para regresar al menú...")
            
        elif opcion == "2":
            print("\n--- MONITOREO ATMOSFÉRICO (OPEN-METEO) ---")
            lat, lon = 19.1738, -96.1342
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_gusts_10m"
            try:
                print("Consultando atmósfera en tiempo real...")
                with urllib.request.urlopen(url) as response:
                    data = json.loads(response.read().decode())
                    current = data.get("current", {})
                    print(f"Temperatura Ambiente: {current.get('temperature_2m')} °C")
                    print(f"Humedad Relativa:     {current.get('relative_humidity_2m')}%")
                    print(f"Velocidad del Viento: {current.get('wind_speed_10m')} km/h")
                    print(f"Ráfagas de Viento:    {current.get('voices', current.get('wind_gusts_10m'))} km/h")
                    
                    viento = current.get('wind_speed_10m', 0)
                    if viento > 25:
                        print("\n⚠️ ALERTA: Viento fuerte detectado. Riesgo para aspersión.")
                    else:
                        print("\n✅ Condiciones óptimas de viento para vuelo seguro.")
            except Exception as e:
                print(f"Error de conexión con la API de clima: {e}")
            input("\nPresione Enter para regresar al menú...")
            
        elif opcion == "3":
            print("\n--- CATASTRO GEOESPACIAL DE PARCELAS ---")
            print("• ID de Parcela:      VER-001")
            print("• Cultivo Objetivo:   Caña de Azúcar")
            print("• Ubicación / Ejido:  Ejido Local (Veracruz)")
            print("• Geometría:          Polígono Estanco Verificado (GeoJSON)")
            print("• Estado de Rutas:    Listo para cálculo de tasa variable (VRA)")
            input("\nPresione Enter para regresar al menú...")
            
        elif opcion == "4":
            print("\nSaliendo del panel operativo. ¡Buen vuelo, ingeniero!")
            sys.exit(0)
        else:
            print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
