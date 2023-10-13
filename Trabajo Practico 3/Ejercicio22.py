def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

numeros_pares = 0

while True:
    numero = int(input("Ingrese un número entero (o -1 para terminar): "))

    if numero == -1:
        break

    if numero % 2 == 0:
        numeros_pares += 1

    suma_de_digitos = suma_digitos(abs(numero))
    print(f"La suma de los dígitos de {numero} es: {suma_de_digitos}")

print(f"Total de números pares ingresados: {numeros_pares}")
