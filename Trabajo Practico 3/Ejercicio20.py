sumatoria = 0

while True:
    numero = int(input("Ingrese un número entero (o 0 para terminar): "))
    if numero == 0:
        break
    sumatoria += numero

print(f"La sumatoria de todos los números ingresados es: {sumatoria}")
