# =========================================================================
# SIMULADOR NEURONAL PREDICTIVO (TÉRMICO Y ATMOSFÉRICO) - STR-002 H3
# =========================================================================
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def entrenar_modelo_predictivo():
    print("Iniciando entrenamiento del modelo neuronal con variables de parcela...")
    
    # Datos de entrenamiento sintéticos basados en física y clima extremo:
    # Entradas: [Temp_Ambiente (°C), Viento (m/s), MTOW (kg), Corriente_Total (A)]
    np.random.seed(42)
    n_samples = 2000
    
    X_train = np.column_stack([
        np.random.uniform(20.0, 45.0, n_samples),  # Temp Ambiente (°C)
        np.random.uniform(0.0, 15.0, n_samples),   # Viento / Ráfagas (m/s)
        np.random.uniform(45.0, 60.0, n_samples),  # Peso Total (MTOW kg)
        np.random.uniform(170.0, 220.0, n_samples) # Corriente Total (A)
    ])
    
    # Salida objetivo: Temperatura Final de Celdas 18S (°C)
    Y_train = 25.0 + (0.58 * X_train[:, 0]) - (0.15 * X_train[:, 1]) + (0.04 * X_train[:, 2]) + (0.13 * X_train[:, 3]) + np.random.normal(0, 0.4, n_samples)
    
    # Arquitectura de Red Neuronal Multicapa (MLP)
    model = Sequential([
        Dense(64, activation='relu', input_shape=(4,)),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    model.fit(X_train, Y_train, epochs=30, batch_size=32, verbose=0)
    
    print("¡Modelo neuronal entrenado con éxito bajo escenarios de estrés!")
    return model

if __name__ == "__main__":
    modelo = entrenar_modelo_predictivo()
    modelo.save("str002_modelo_neuronal_termico.h5")
    print("Modelo guardado exitosamente en 'str002_modelo_neuronal_termico.h5'")
