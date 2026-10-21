# GENERADOR DE PLANOS DXF PARA CORTE CNC — STR-002 H3 v3.0
# Genera el chasis central octogonal en Fibra de Carbono 3mm

import ezdxf
import math

def generar_dxf_chasis():
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()

    # Perímetro Octogonal Central (Radio 180 mm)
    r = 180.0
    puntos = [
        (r * 0.92, r * 0.38), (r * 0.38, r * 0.92),
        (-r * 0.38, r * 0.92), (-r * 0.92, r * 0.38),
        (-r * 0.92, -r * 0.38), (-r * 0.38, -r * 0.92),
        (r * 0.38, -r * 0.92), (r * 0.92, -r * 0.38),
        (r * 0.92, r * 0.38) # Cierre
    ]
    msp.add_lwpolyline(puntos, close=True)

    # Perforaciones para Abrazaderas de Brazos H3 (8 brazos Coaxiales)
    angulos = [0, 45, 90, 135, 180, 225, 270, 315]
    for ang in angulos:
        rad = math.radians(ang)
        # Barrenos M4 para fijación de abrazaderas de 50mm
        x1 = 140.0 * math.cos(rad)
        y1 = 140.0 * math.sin(rad)
        msp.add_circle((x1, y1), radius=2.1) # Diámetro 4.2mm (M4)

    # Ventana central de disipación para Cube Orange+ (80x80 mm)
    ventana_puntos = [(-40.0, -40.0), (40.0, -40.0), (40.0, 40.0), (-40.0, 40.0), (-40.0, -40.0)]
    msp.add_lwpolyline(ventana_puntos, close=True)

    doc.saveas("cad/chasis_central_cfrp_3mm_str002_h3.dxf")
    print("✅ Archivo cad/chasis_central_cfrp_3mm_str002_h3.dxf generado con éxito.")

if __name__ == '__main__':
    generar_dxf_chasis()
