contraseña_correcta = "password123"  # Contraseña correcta

while True:
    contraseña_ingresada = input("Ingrese la contraseña: ")

    if contraseña_ingresada == contraseña_correcta:
        print("¡Contraseña correcta! Acceso concedido.")
        break  # Salir del bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Intente de nuevo.")
