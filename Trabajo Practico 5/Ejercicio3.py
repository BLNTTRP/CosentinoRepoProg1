def validar_dni(dni):
    # Verifica si el DNI tiene 7 u 8 dígitos
    return len(dni) in (7, 8) and dni.isdigit()

def generar_identificador(nombre, dni):
    # Divide el nombre en palabras y toma el primer nombre
    primer_nombre = nombre.split()[0]
    
    # Toma la longitud del apellido
    apellido = nombre.split()[-1]
    longitud_apellido = len(apellido)
    
    # Toma los 3 primeros dígitos del DNI
    tres_primeros_digitos_dni = dni[:3]
    
    # Genera el identificador
    identificador = primer_nombre + str(longitud_apellido) + tres_primeros_digitos_dni
    return identificador

socios = []

while True:
    nombre = input("Nombre del socio (o dejar vacío para finalizar): ")
    
    if not nombre:
        break  # Salir del bucle si se ingresa un nombre vacío
    
    dni = input("DNI del socio: ")
    
    # Validar el DNI
    if not validar_dni(dni):
        print("DNI no válido. Debe tener 7 u 8 dígitos.")
        continue  # Volver a pedir el DNI
    
    identificador = generar_identificador(nombre, dni)
    socios.append(identificador)

# Imprimir identificadores de los socios
for identificador in socios:
    print(f"ID -> {identificador}")
