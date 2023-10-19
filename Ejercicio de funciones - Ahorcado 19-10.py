import random

# Lista de palabras para adivinar
palabras = ["python", "programacion", "tecnologia", "desarrollo", "computadora", "inteligencia"]

def seleccionar_palabra():
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
    return tablero

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    intentos = 6
    letras_adivinadas = []
    
    print("¡Bienvenido al juego del ahorcado!")
    
    while True:
        tablero = mostrar_tablero(palabra_secreta, letras_adivinadas)
        print(tablero)
        
        if tablero == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra: " + palabra_secreta)
            break
        
        if intentos == 0:
            print("¡Has perdido! La palabra era: " + palabra_secreta)
            break
        
        letra = input("Adivina una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa una letra válida.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra_secreta:
            print("Adivinaste una letra correctamente.")
            letras_adivinadas.append(letra)
        else:
            print("Letra incorrecta, te quedan", intentos, "intentos.")
            intentos -= 1

if __name__ == "__main__":
    jugar_ahorcado()
