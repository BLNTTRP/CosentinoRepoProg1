import math

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_circulo(radio):
    return math.pi * radio**2

# Solicitar al usuario qué área desea calcular
opcion = input("¿Desea calcular el área de un triángulo (T) o un círculo (C)? ").upper()

if opcion == "T":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area}")
elif opcion == "C":
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area}")
else:
    print("Opción no válida. Por favor, ingrese 'T' para triángulo o 'C' para círculo.")
