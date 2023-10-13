frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Contar la cantidad de veces que aparece la letra en la frase
contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")
