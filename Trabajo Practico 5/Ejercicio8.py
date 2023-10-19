import math

def calcular_area_y_perimetro(radio):
    # Calcular el área de la circunferencia
    area = math.pi * radio ** 2

    # Calcular el perímetro (circunferencia) de la circunferencia
    perimetro = 2 * math.pi * radio

    return area, perimetro

def main():
    # Solicitar al usuario que ingrese el radio de la circunferencia
    radio = float(input("Ingrese el radio de la circunferencia: "))

    # Llamar a la función para calcular el área y el perímetro
    area, perimetro = calcular_area_y_perimetro(radio)

    # Mostrar los resultados
    print(f"Área de la circunferencia: {area}")
    print(f"Perímetro de la circunferencia: {perimetro}")

if __name__ == "__main__":
    main()
