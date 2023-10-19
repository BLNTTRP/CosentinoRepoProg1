def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

sumatoria_total = 0
suma_num_ingr = 0

while True:
    numero = int(input("Ingrese un número (o 0 para salir): "))
    if numero == 0:
        break
    suma_num_ingr += numero
    suma = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {suma}")
    sumatoria_total += suma

print(f"La sumatoria total de las sumas de dígitos es: {sumatoria_total}")
print(f"La suma de todos los numeros ingresados es: {suma_num_ingr}")
