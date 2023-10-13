def es_primo(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    # Comprobar si el número es divisible por algún número impar hasta la raíz cuadrada del número
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True

numero = int(input("Ingrese un número entero: "))

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
