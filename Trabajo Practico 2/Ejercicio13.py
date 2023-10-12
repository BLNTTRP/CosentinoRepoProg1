def es_multiplo(mayor, menor):
    return mayor % menor == 0

# Solicitar al usuario dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Validar que los números no sean negativos o nulos
if num1 <= 0 or num2 <= 0:
    print("Por favor, ingrese números enteros positivos.")
else:
    # Encontrar el mayor y el menor
    mayor = max(num1, num2)
    menor = min(num1, num2)

    # Verificar si el mayor es múltiplo del menor
    if es_multiplo(mayor, menor):
        print(f"{mayor} es múltiplo de {menor}.")
    else:
        print(f"{mayor} no es múltiplo de {menor}.")
