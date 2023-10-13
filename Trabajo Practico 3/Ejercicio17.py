def obtener_vocales(frase):
    # Convertir la frase a minúsculas para considerar tanto mayúsculas como minúsculas
    frase = frase.lower()
    # Definir un conjunto para almacenar las vocales
    vocales = set()

    # Iterar sobre cada caracter de la frase
    for caracter in frase:
        if caracter in 'aeiou':
            vocales.add(caracter)

    return vocales

frase = input("Ingrese una frase: ")

# Obtener las vocales de la frase
vocales_frase = obtener_vocales(frase)

print("Vocales en la frase:")
for vocal in vocales_frase:
    print(vocal)
