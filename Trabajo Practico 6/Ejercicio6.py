alumnos_primario = set()
alumnos_secundario = set()

# Ingresar nombres de alumnos de nivel primario
print("Ingresar nombres de alumnos de nivel primario (ingrese 'x' para finalizar):")
while True:
    nombre = input()
    if nombre == 'x':
        break
    alumnos_primario.add(nombre)

# Ingresar nombres de alumnos de nivel secundario
print("Ingresar nombres de alumnos de nivel secundario (ingrese 'x' para finalizar):")
while True:
    nombre = input()
    if nombre == 'x':
        break
    alumnos_secundario.add(nombre)

# a. Informar los nombres de todos los alumnos sin repeticiones
todos_los_alumnos = alumnos_primario.union(alumnos_secundario)
print("Nombres de todos los alumnos (sin repeticiones):")
for nombre in todos_los_alumnos:
    print(nombre)

# b. Informar nombres repetidos entre primario y secundario
nombres_repetidos = alumnos_primario.intersection(alumnos_secundario)
print("Nombres repetidos entre primario y secundario:")
for nombre in nombres_repetidos:
    print(nombre)

# c. Informar nombres de primario que no se repiten en secundario
nombres_primario_no_repetidos = alumnos_primario.difference(alumnos_secundario)
print("Nombres de primario que no se repiten en secundario:")
for nombre in nombres_primario_no_repetidos:
    print(nombre)
