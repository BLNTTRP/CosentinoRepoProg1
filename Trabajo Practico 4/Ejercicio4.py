def es_primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    max_divisor = int(num**0.5) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False

    return True

cantidad_primos = 0

print("Ingrese números mayores que 1 (ingrese 0 para terminar):")

while True:
    numero = int(input("Número: "))

    if numero == 0:
        break

    if es_primo(numero):
        cantidad_primos += 1

print("Cantidad de números primos ingresados:", cantidad_primos)
