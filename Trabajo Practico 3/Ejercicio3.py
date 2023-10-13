numero = int(input("Ingrese un número entero positivo: "))

# Asegurarse de que el número sea positivo
if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
    resultado = ', '.join(impares)
    print(f"Números impares desde 1 hasta {numero}: {resultado}")
