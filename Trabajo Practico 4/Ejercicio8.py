while True:
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        print("Saliendo del programa.")
        break
    elif opcion == "1":
        print("Ha elegido la Opción 1.")
    elif opcion == "2":
        print("Ha elegido la Opción 2.")
    elif opcion == "3":
        print("Ha elegido la Opción 3.")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
