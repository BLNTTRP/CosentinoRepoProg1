numero = int(input("Ingrese un número entero mayor que cero: "))

if numero <= 0:
    print("Por favor, ingrese un número entero mayor que cero.")
else:
    print(f"Divisores de {numero}:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
