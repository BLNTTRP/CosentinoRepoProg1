def login(nombre_usuario, contrasena, intentos):
    # Definir el nombre de usuario y contraseña correctos
    usuario_correcto = "usuario1"
    contrasena_correcta = "asdasd"

    if nombre_usuario == usuario_correcto and contrasena == contrasena_correcta:
        # Las credenciales son correctas, devuelve Verdadero
        return True, intentos
    else:
        # Las credenciales son incorrectas, incrementa el contador de intentos
        intentos += 1
        return False, intentos

def main():
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        nombre_usuario = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")

        resultado, intentos = login(nombre_usuario, contrasena, intentos)

        if resultado:
            print("Inicio de sesión exitoso.")
            break
        else:
            print("Credenciales incorrectas. Intentos restantes:", max_intentos - intentos)

    if intentos >= max_intentos:
        print("Exceso de intentos. Bloqueo de cuenta.")

if __name__ == "__main__":
    main()
