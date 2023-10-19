def longitud_palabras(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Crear un diccionario para almacenar las palabras y sus longitudes
    resultado = {}
    
    for palabra in palabras:
        # Eliminar signos de puntuación alrededor de la palabra (si es necesario)
        palabra = palabra.strip('.,!?')
        # Almacenar la palabra y su longitud en el diccionario
        resultado[palabra] = len(palabra)
    
    return resultado

# Ejemplo de uso:
frase = "Esta es una frase de ejemplo, con algunas palabras."
resultado = longitud_palabras(frase)
print(resultado)
