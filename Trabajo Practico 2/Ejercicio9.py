nombre = input("Ingresa el nombre a buscar: ")
while True:
    sexo = input("Ingresa tu genero (H o M): ")
    sexo = sexo.upper()
    if sexo != "H" and sexo != "M":
        print("Caracter inválido. Reintenta")
    else:
        break

nombre = nombre.title()

if sexo == "M" and nombre[0] < 'M':
    print("Perteneces al grupo A.")
elif sexo == "M" and nombre[0] >= 'M':
    print("Perteneces al grupo B.")

if sexo == "H" and nombre[0] > 'N':
    print("Perteneces al grupo A.")
elif sexo == "H" and nombre[0] <= 'N':
    print("Perteneces al grupo B.")