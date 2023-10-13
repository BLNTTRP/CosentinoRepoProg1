cantidad_numeros = int(input("¿Cuántos números va a introducir? "))

numeros_negativos = 0

for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    if numero < 0:
        numeros_negativos += 1

print(f"Números negativos introducidos: {numeros_negativos}")
