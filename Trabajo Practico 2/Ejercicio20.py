def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Solicitar al usuario las cuatro notas
notas = []
for i in range(4):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

# Calcular el promedio de las notas
promedio = calcular_promedio(notas)

# Determinar si aprueba o reprueba
if promedio >= 6:
    print(f"El alumno tiene un promedio de {promedio:.2f} y ha aprobado el curso.")
else:
    print(f"El alumno tiene un promedio de {promedio:.2f} y ha reprobado el curso.")
