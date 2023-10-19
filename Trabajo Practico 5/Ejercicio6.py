def agregar_espacios(texto):
    # Inicializar una cadena vacía para almacenar el resultado
    resultado = ""
    
    # Iterar a través de cada caracter en el texto
    for caracter in texto:
        resultado += caracter + " "
    
    return resultado

def main():
    # Solicitar al usuario que ingrese un texto
    texto = input("Ingrese un texto: ")

    # Llamar a la función para agregar espacios
    texto_con_espacios = agregar_espacios(texto)

    # Mostrar el texto con espacios adicionales
    print("Texto con espacios adicionales:")
    print(texto_con_espacios)

if __name__ == "__main__":
    main()
