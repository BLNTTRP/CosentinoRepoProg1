def validar_dni(numero_dni):
    # Convierte el número de DNI a una cadena para contar la cantidad de dígitos
    dni_str = str(numero_dni)
    
    # Verifica si la longitud de la cadena está entre 7 y 8 dígitos
    if 7 <= len(dni_str) <= 8:
        return True
    else:
        return False

# Ejemplo de uso
numero_dni = int(input("Ingresa un numero de documento: "))
es_valido = validar_dni(numero_dni)
if es_valido:
    print(f"El número de DNI {numero_dni} es válido.")
else:
    print(f"El número de DNI {numero_dni} no es válido.")
