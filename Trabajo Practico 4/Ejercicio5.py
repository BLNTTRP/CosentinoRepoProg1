def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def imprimir_anios_bisiestos_y_multiplos_de_10(year_inicio, year_fin):
    print(f"Años bisiestos y múltiplos de 10 en el rango {year_inicio} - {year_fin}:")
    for year in range(year_inicio, year_fin + 1):
        if es_bisiesto(year) and year % 10 == 0:
            print(year)

year_inicio = int(input("Ingrese el año de inicio: "))
year_fin = int(input("Ingrese el año de fin: "))

imprimir_anios_bisiestos_y_multiplos_de_10(year_inicio, year_fin)
