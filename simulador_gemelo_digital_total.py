# ==============================================================================
# PERLACOLABS — SIMULADOR MULTISECTORIAL Y GRÁFICAS DINÁMICAS (STR-002 H3)
# ==============================================================================

import os
import json
import datetime
import random
import urllib.request
import matplotlib.pyplot as plt

class SimuladorGraficoDinamico:
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Variedades de cultivos, parcelas y tipos de sopa líquida (Agroquímicos / Maduradores)
        self.escenarios_agricolas = [
            {
                "parcela": "Parcela Central - Veracruz",
                "lat": 19.3456, "lon": -96.4521,
                "cultivo": "Caña de Azúcar",
                "variedad": "CP 72-2086",
                "hectareas": 18.5,
                "sopa_liquida": "Madurador Enzimático (Glifosato / Etefón)",
                "volumen_base_l_ha": 35.0
            },
            {
                "parcela": "Parcela Norte - Úrsulo Galván",
                "lat": 19.3721, "lon": -96.4832,
                "cultivo": "Caña de Azúcar",
                "variedad": "Mex 69-290",
                "hectareas": 24.0,
                "sopa_liquida": "Fungicida Sistémico (Tebuconazole 25%)",
                "volumen_base_l_ha": 40.0
            },
            {
                "parcela": "Parcela Experimental - Limón Persa",
                "lat": 18.4521, "lon": -95.3120,
                "cultivo": "Citricos (Limón Persa)",
                "variedad": "Persa Sin Semilla",
                "hectareas": 12.0,
                "sopa_liquida": "Foliar Nutricional NPK + Microquelatados",
                "volumen_base_l_ha": 50.0
            }
        ]

    def consultar_clima_open_meteo(self, lat, lon):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=4) as resp:
                data = json.loads(resp.read().decode())
                current = data.get("current", {})
                return {
                    "temperatura_c": current.get("temperature_2m", 29.0),
                    "humedad_pct": current.get("relative_humidity_2m", 65.0),
                    "viento_ms": current.get("wind_speed_10m", 3.2),
                    "fuente": "Open-Meteo API en vivo"
                }
        except Exception:
            return {"temperatura_c": 31.0, "humedad_pct": 60.0, "viento_ms": 4.5, "fuente": "Fallback de Red"}

    def generar_grafica_analitica(self, datos):
        """Genera una gráfica elegante con Matplotlib basada en las variables dinámicas."""
        os.makedirs("telemetria_campo", exist_ok=True)
        
        # Datos para graficar
        etiquetas = ['Tasa Base (L/ha)', 'Dosis VRA Ajustada', 'Caudal CDA (L/min)']
        valores = [
            datos["dosificacion"]["volumen_base_l_ha"],
            datos["dosificacion"]["tasa_vra_ajustada_l_ha"],
            datos["dosificacion"]["caudal_operativo_l_min"]
        ]
        
        plt.figure(figsize=(8, 5), dpi=300)
        bars = plt.bar(etiquetas, valores, color=['#2980b9', '#27ae60', '#e67e22'], width=0.6)
        
        plt.title(f"Dinámica VRA y Sopa Líquida — {datos['cultivo']} ({datos['variedad']})", fontsize=11, fontweight='bold', pad=12)
        plt.ylabel("Volumen / Caudal Operativo", fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Añadir valores sobre las barras
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.5, f'{height:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
            
        grafica_path = "telemetria_campo/grafica_dinamica_operacion.png"
        plt.savefig(grafica_path, bbox_inches='tight')
        plt.close()
        print(f"📊 Gráfica actualizada generada con éxito en: {grafica_path}")

    def ejecutar(self):
        escenario = random.choice(self.escenarios_agricolas)
        clima = self.consultar_clima_open_meteo(escenario["lat"], escenario["lon"])
        
        # Cálculos VRA dinámicos basados en viento y temperatura
        factor_climatico = 1.0 + ((clima["viento_ms"] - 3.0) * 0.02)
        tasa_vra_ajustada = escenario["volumen_base_l_ha"] * factor_climatico
        volumen_total = tasa_vra_ajustada * escenario["hectareas"]
        
        resultado = {
            "timestamp": self.timestamp,
            "parcela": escenario["parcela"],
            "cultivo": escenario["cultivo"],
            "variedad": escenario["variedad"],
            "hectareas": escenario["hectareas"],
            "sopa_liquida": escenario["sopa_liquida"],
            "clima": clima,
            "dosificacion": {
                "volumen_base_l_ha": escenario["volumen_base_l_ha"],
                "tasa_vra_ajustada_l_ha": round(tasa_vra_ajustada, 2),
                "caudal_operativo_l_min": 16.0,
                "volumen_total_mezcla_l": round(volumen_total, 2)
            },
            "mecanica_dron": {
                "modelo": "STR-002 H3 v3.5 (Octocóptero Coaxial X8)",
                "factor_seguridad_7075": 4.17,
                "precision_rtk_mm": round(random.uniform(8.0, 11.5), 1)
            }
        }

        with open("telemetria_campo/reporte_dinamico_actualizado.json", "w", encoding="utf-8") as f:
            json.dump(resultado, f, indent=4)
            
        self.generar_grafica_analitica(resultado)
        print(f"✅ Simulación completada para [{escenario['cultivo']} - {escenario['variedad']}]")
        return resultado

if __name__ == "__main__":
    sim = SimuladorGraficoDinamico()
    sim.ejecutar()
