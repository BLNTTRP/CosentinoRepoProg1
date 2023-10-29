def es_potencia(n, b):
    if n <= 0 or b <= 0:
        return False

    while n > 1:
        if n % b != 0:
            return False
        n = n // b
    return True

# Solicitar al usuario dos enteros
n = int(input("Ingrese un número entero n: "))
b = int(input("Ingrese un número entero b: "))

# Comprobar si n es una potencia de b y mostrar el resultado
if es_potencia(n, b):
    print(f"{n} es una potencia de {b}.")
else:
    print(f"{n} no es una potencia de {b}.")
