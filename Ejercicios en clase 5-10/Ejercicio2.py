def contar_digitos_pares_impares(numero):
    pares = 0
    impares = 0

    # Iterar sobre cada dígito del número
    while numero > 0:
        digito = numero % 10  # Obtener el último dígito
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10  # Eliminar el último dígito

    return pares, impares

# Inicializar contadores
total_pares = 0
total_impares = 0

# Solicitar al usuario que ingrese números hasta que ingrese 0
while True:
    numero = int(input("Ingrese un número entero positivo (o 0 para terminar): "))

    if numero == 0:
        break

    # Contar dígitos pares e impares para el número actual
    pares, impares = contar_digitos_pares_impares(numero)

    # Actualizar los contadores totales
    total_pares += pares
    total_impares += impares

    print(f"Para el número {numero}, hay {pares} dígitos pares y {impares} dígitos impares.")

# Mostrar el total de dígitos pares e impares leídos
print("Total de dígitos pares leídos:", total_pares)
print("Total de dígitos impares leídos:", total_impares)
