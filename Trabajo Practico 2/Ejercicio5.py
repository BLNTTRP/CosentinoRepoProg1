letra = input("Ingresa una letra: ")

letra = letra.upper()

if len(letra) > 1 or len(letra) < 1:
    print("No es posible procesar el dato.")
elif letra == "A":
    print("Es vocal.")
elif letra == "E":
    print("Es vocal.")
elif letra == "I":
    print("Es vocal.")
elif letra == "O":
    print("Es vocal.")
elif letra == "U":
    print("Es vocal.")
else:
    print("No es vocal.")