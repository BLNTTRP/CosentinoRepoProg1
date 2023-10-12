# Solicitar al usuario el total de horas trabajadas en el mes y el salario por hora
horas_trabajadas_mes = float(input("Ingrese el total de horas trabajadas en el mes: "))
salario_por_hora = float(input("Ingrese el salario por hora: "))

# Calcular si se trabajaron horas extras y cuántas
jornada_minima = 48
horas_extras = max(0, horas_trabajadas_mes - jornada_minima)

# Calcular el salario total
salario_total = (jornada_minima * salario_por_hora) + (horas_extras * salario_por_hora * 1.10)

# Mostrar las horas extras trabajadas y el salario total
print("Horas extras trabajadas:", horas_extras)
print("Salario total:", salario_total)
