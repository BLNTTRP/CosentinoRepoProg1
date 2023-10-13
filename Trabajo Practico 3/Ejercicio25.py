def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    factorial_resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es {factorial_resultado}.")
