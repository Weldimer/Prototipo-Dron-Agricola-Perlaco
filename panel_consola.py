import urllib.request
import json
import sys
import datetime

def mostrar_banner():
    print("==========================================================")
    print("      PANEL DE CONTROL TÉCNICO AVANZADO — STR-002 H3     ")
    print("      Gemelo Digital & Simulación de Vuelo (MTOW 60 kg)   ")
    print("==========================================================")

def calcular_consumo_electrico():
    print("\n--- SIMULADOR DE CONSUMO Y AUTONOMÍA (BUS HV 18S) ---")
    try:
        payload_kg = float(input("Ingrese la carga útil actual (Líquido/Insumo en kg, máx 25 kg): "))
        if payload_kg < 0 or payload_kg > 30:
            print("⚠️ Advertencia: Carga fuera del rango nominal de diseño (0 - 25 kg).")
            return
        
        peso_base = 35.0  # Peso vacío del dron con aviónica y baterías (kg)
        mtow_actual = peso_base + payload_kg
        voltaje_nominal = 66.6  # Bus 18S
        
        # Estimación física para octocóptero agrícola (eficiencia de motores 30")
        corriente_total = mtow_actual * 2.15 
        corriente_por_motor = corriente_total / 8
        potencia_w = corriente_total * voltaje_nominal
        
        # Batería inteligente 18S (~30 Ah) con DoD 80%
        capacidad_bateria_ah = 30.0
        autonomia_minutos = (capacidad_bateria_ah / corriente_total) * 60 * 0.8
        
        print(f"\n[RESULTADOS DE SIMULACIÓN ELÉCTRICA]")
        print(f"• Peso Total en Vuelo (MTOW): {mtow_actual:.2f} kg")
        print(f"• Corriente Total del Bus HV: {corriente_total:.2f} A")
        print(f"• Corriente por Motor (x8):   {corriente_por_motor:.2f} A / motor")
        print(f"• Potencia Eléctrica Requerida: {potencia_w:.2f} W")
        print(f"• Autonomía Estimada (DoD 80%): {autonomia_minutos:.1f} minutos")
        
        # Registro en bitácora local de CloudShell
        registro = {
            "timestamp": str(datetime.datetime.now()),
            "payload_kg": payload_kg,
            "mtow_kg": mtow_actual,
            "corriente_total_a": round(corriente_total, 2),
            "autonomia_min": round(autonomia_minutos, 1)
        }
        
        try:
            with open("bitacora_operativa.json", "a") as f:
                f.write(json.dumps(registro) + "\n")
            print("✅ Datos guardados en bitácora local (bitacora_operativa.json).")
        except Exception:
            pass
            
    except ValueError:
        print("❌ Error: Ingrese un valor numérico válido.")
    input("\nPresione Enter para regresar al menú...")

def menu():
    while True:
        mostrar_banner()
        print("\nSeleccione una opción de ingeniería:")
        print("1. Estado del Gemelo Digital (FEA & Materiales)")
        print("2. Monitoreo Atmosférico en Tiempo Real (Clima - Veracruz)")
        print("3. Catastro Geoespacial de Parcelas y Rutas VRA")
        print("4. Simulador de Consumo Eléctrico y Autonomía (HV 18S)")
        print("5. Salir")
        
        opcion = input("\nIngrese el número de opción: ").strip()
        
        if opcion == "1":
            print("\n--- ESTADO DEL GEMELO DIGITAL Y HARDWARE ---")
            print("• Factor de Seguridad (FEA): 3.46 (Aluminio 7075-T6)")
            print("• Esfuerzo de Von Mises:    145.20 MPa vs 503 MPa límite")
            print("• Bus de Potencia HV:       66.6V / 18S (~126 A Nominal)")
            print("• Tolerancia Mecánica P-01: Ø24.0 mm H7 (Ajuste de precisión)")
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
                    print(f"Ráfagas de Viento:    {current.get('wind_gusts_10m')} km/h")
                    
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
            calcular_consumo_electrico()
            
        elif opcion == "5":
            print("\nSaliendo del panel operativo. ¡Buen vuelo, ingeniero!")
            sys.exit(0)
        else:
            print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
