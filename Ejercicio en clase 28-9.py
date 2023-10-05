def calcular_porcentaje_aprobados(aprobados, total_alumnos):
    if total_alumnos == 0:
        return 0
    return (aprobados / total_alumnos) * 100

# Solicitar la fecha al usuario
fecha_input = input("Ingrese la fecha en formato 'día, DD/MM': ").strip().lower()

# Diccionario que mapea los días de la semana a los niveles correspondientes
dias_niveles = {
    'lunes': 'inicial',
    'martes': 'intermedio',
    'miércoles': 'avanzado',
    'jueves': 'práctica hablada',
    'viernes': 'inglés para viajeros'
}

# Validar el formato de la fecha
try:
    dia_semana, fecha = fecha_input.split(', ')
    dia, mes = map(int, fecha.split('/'))
except ValueError:
    print("Error: formato de fecha incorrecto.")
    exit()

# Validar la fecha
if mes > 12 or dia > 31:
    print("Error: fecha no válida.")
    exit()

# Obtener el nivel del día de la semana
nivel = dias_niveles.get(dia_semana, None)

# Procesar según el nivel
if nivel in ['inicial', 'intermedio', 'avanzado']:
    # Preguntar si se tomaron exámenes
    examenes = input("¿Se tomaron exámenes? (sí/no): ").strip().lower()

    if examenes == 'sí':
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        total_alumnos = int(input("Ingrese la cantidad total de alumnos: "))

        porcentaje_aprobados = calcular_porcentaje_aprobados(aprobados, total_alumnos)
        print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")
    else:
        print("No se tomaron exámenes.")

elif nivel == 'práctica hablada':
    asistencia_porcentaje = float(input("Ingrese el porcentaje de asistencia a clase: "))

    if asistencia_porcentaje > 50:
        print("Asistió la mayoría.")
    else:
        print("No asistió la mayoría.")

elif nivel == 'inglés para viajeros':
    if (mes == 1 and dia == 1) or (mes == 7 and dia == 1):
        print("Comienzo de nuevo ciclo")
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel_por_alumno = float(input("Ingrese el arancel en $ por cada alumno: "))

        ingreso_total = cantidad_alumnos * arancel_por_alumno
        print(f"Ingreso total en $: {ingreso_total}")

else:
    print("Error: día de la semana no válido para procesar observaciones.")
