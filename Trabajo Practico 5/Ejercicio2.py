def longitud_ultima_palabra(cadena):
    # Elimina espacios en blanco al principio y al final del string
    cadena = cadena.strip()
    
    # Divide la cadena en palabras utilizando espacios como separadores
    palabras = cadena.split()
    
    # Verifica si hay palabras en la cadena
    if palabras:
        # Retorna la longitud de la última palabra
        return len(palabras[-1])
    else:
        # Si no hay palabras, retorna 0
        return 0

# Ejemplo de uso
cadena = input("Ingresa una frase: ")
longitud = longitud_ultima_palabra(cadena)
print(f"La longitud de la última palabra es: {longitud}")
