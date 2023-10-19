def es_multiplo(numero1, numero2):
    # Verifica si numero1 es múltiplo de numero2
    if numero2 == 0:
        return False  # Evita división por cero
    return numero1 % numero2 == 0

# Solicitar dos números enteros al usuario
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Verificar si alguno de los números es múltiplo del otro
if es_multiplo(numero1, numero2):
    print(f"{numero1} es múltiplo de {numero2} o viceversa.")
else:
    print(f"{numero1} no es múltiplo de {numero2} y viceversa.")
