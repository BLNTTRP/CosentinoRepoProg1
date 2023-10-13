mayor_numero = float('-inf')

while True:
    numero = int(input("Ingrese un número entero positivo (o 0 para terminar): "))
    if numero == 0:
        break
    elif numero > mayor_numero:
        mayor_numero = numero

if mayor_numero == float('-inf'):
    print("No se ha ingresado ningún número entero positivo.")
else:
    print(f"El mayor número ingresado es: {mayor_numero}")
