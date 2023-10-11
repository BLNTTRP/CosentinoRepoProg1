def calcular_hora_llegada(hora_salida, minutos_salida, segundos_salida, tiempo_viaje):
    # Convertir la hora de salida a segundos
    tiempo_salida_segundos = hora_salida * 3600 + minutos_salida * 60 + segundos_salida
    
    # Calcular el tiempo de llegada en segundos
    tiempo_llegada_segundos = tiempo_salida_segundos + tiempo_viaje
    
    # Calcular la hora de llegada en horas, minutos y segundos
    horas_llegada = tiempo_llegada_segundos // 3600
    minutos_llegada = (tiempo_llegada_segundos % 3600) // 60
    segundos_llegada = tiempo_llegada_segundos % 60
    
    return horas_llegada, minutos_llegada, segundos_llegada

# Datos de salida desde la ciudad A
hora_salida = 8  # Hora de salida (formato de 24 horas)
minutos_salida = 30  # Minutos de salida
segundos_salida = 0  # Segundos de salida

# Tiempo de viaje en segundos
tiempo_viaje = 7200  # 7200 segundos = 2 horas

# Calcular la hora de llegada
hora_llegada, minutos_llegada, segundos_llegada = calcular_hora_llegada(hora_salida, minutos_salida, segundos_salida, tiempo_viaje)

# Mostrar la hora de llegada
print(f"Hora de llegada a la ciudad B: {hora_llegada:02d}:{minutos_llegada:02d}:{segundos_llegada:02d}")
