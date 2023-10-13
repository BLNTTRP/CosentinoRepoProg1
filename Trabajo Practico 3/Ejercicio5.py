def calcular_capital(cantidad, tasa_interes, años):
    capital_por_año = []
    for i in range(años):
        cantidad *= (1 + tasa_interes)
        capital_por_año.append(cantidad)
    return capital_por_año

# Solicitar al usuario los datos de la inversión
cantidad_invertida = float(input("Ingrese la cantidad a invertir: $"))
tasa_interes_anual = float(input("Ingrese el interés anual en porcentaje (por ejemplo, 5 para el 5%): ")) / 100
años = int(input("Ingrese el número de años: "))

# Calcular el capital obtenido cada año
capital_por_año = calcular_capital(cantidad_invertida, tasa_interes_anual, años)

# Mostrar el capital obtenido cada año
for i, capital in enumerate(capital_por_año):
    print(f"Año {i + 1}: ${capital:.2f}")
