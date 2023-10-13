def encriptar_mensaje(mensaje, corrimiento):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Alfabeto en mayúsculas
    resultado = ''

    for letra in mensaje:
        if letra.isalpha():  # Verificar si es una letra
            es_mayuscula = letra.isupper()
            letra = letra.upper()
            indice = alfabeto.index(letra)
            nuevo_indice = (indice + corrimiento) % 26
            nueva_letra = alfabeto[nuevo_indice]

            if not es_mayuscula:
                nueva_letra = nueva_letra.lower()

            resultado += nueva_letra
        else:
            resultado += letra

    return resultado

# Solicitar al usuario el corrimiento y los mensajes a encriptar
corrimiento = int(input("Ingrese la cantidad de lugares a correr las letras: "))

for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i + 1}: ")
    mensaje_encriptado = encriptar_mensaje(mensaje, corrimiento)
    print(f"Mensaje encriptado {i + 1}: {mensaje_encriptado}")
