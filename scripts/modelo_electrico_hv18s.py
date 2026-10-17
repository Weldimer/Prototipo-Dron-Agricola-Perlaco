def calcular_sistema_hv18s(potencia_total_w=14000.0, capacidad_ah=30.0):
    celdas_serie = 18
    voltaje_nominal = celdas_serie * 3.7
    voltaje_maximo = celdas_serie * 4.2
    corriente_nominal = potencia_total_w / voltaje_nominal
    energia_wh = capacidad_ah * voltaje_nominal
    
    print(f"Voltaje Nominal: {voltaje_nominal:.1f} V | Voltaje Máx: {voltaje_maximo:.1f} V")
    print(f"Corriente Nominal: {corriente_nominal:.2f} A | Energía: {energia_wh:.2f} Wh")
    return corriente_nominal, energia_wh

if __name__ == "__main__":
    calcular_sistema_hv18s()
