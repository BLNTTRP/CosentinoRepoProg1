def calcular_anios_pasados_o_faltantes(year_actual, year_objetivo):
    if year_actual > year_objetivo:
        return year_actual - year_objetivo, "años pasados"
    elif year_actual < year_objetivo:
        return year_objetivo - year_actual, "años faltantes"
    else:
        return 0, "Los años son iguales"

# Solicitar al usuario el año actual y el año objetivo
year_actual = int(input("Ingrese el año actual: "))
year_objetivo = int(input("Ingrese un año cualquiera: "))

# Calcular años pasados o faltantes
anios, mensaje = calcular_anios_pasados_o_faltantes(year_actual, year_objetivo)

# Mostrar el resultado
print(f"{anios} {mensaje} desde el año {min(year_actual, year_objetivo)}.")
