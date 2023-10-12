while True:
    usuario = input("Ingresa el nombre de usuario: ")
    if usuario == "Gwenevere":
        contra = input("Contraseña: ")
        if contra == "excalibur":
            print("Acceso concedido. Puede ingresar a Camelot.")
            break
        else:
            print("Acceso denegado. Reintente")
    else:
        print("Usuario incorrecto. Reintente")