def agregar_pasajero(lista_pasajeros):
    nombre = input("Ingrese el nombre del pasajero: ")
    dni = int(input("Ingrese el DNI del pasajero: "))
    destino = input("Ingrese el destino del pasajero: ")
    lista_pasajeros.append((nombre, dni, destino))
    print("Pasajero agregado con éxito.")

def agregar_ciudad(lista_ciudades):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el país al que pertenece la ciudad: ")
    lista_ciudades.append((ciudad, pais))
    print("Ciudad agregada con éxito.")

def buscar_destino_por_dni(lista_pasajeros, dni):
    for pasajero in lista_pasajeros:
        if pasajero[1] == dni:
            return pasajero[2]
    return None

def contar_pasajeros_por_ciudad(lista_pasajeros, ciudad):
    contador = 0
    for pasajero in lista_pasajeros:
        if pasajero[2] == ciudad:
            contador += 1
    return contador

def buscar_pais_por_dni(lista_pasajeros, lista_ciudades, dni):
    destino = buscar_destino_por_dni(lista_pasajeros, dni)
    if destino is not None:
        for ciudad, pais in lista_ciudades:
            if ciudad == destino:
                return pais
    return None

def contar_pasajeros_por_pais(lista_pasajeros, lista_ciudades, pais):
    contador = 0
    for ciudad, pais_ciudad in lista_ciudades:
        if pais_ciudad == pais:
            contador += contar_pasajeros_por_ciudad(lista_pasajeros, ciudad)
    return contador

def main():
    lista_pasajeros = []
    lista_ciudades = []
    
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar pasajero")
        print("2. Agregar ciudad")
        print("3. Ver a qué ciudad viaja un pasajero por su DNI")
        print("4. Mostrar la cantidad de pasajeros que viajan a una ciudad")
        print("5. Ver a qué país viaja un pasajero por su DNI")
        print("6. Mostrar cuántos pasajeros viajan a un país")
        print("7. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            agregar_pasajero(lista_pasajeros)
        elif opcion == "2":
            agregar_ciudad(lista_ciudades)
        elif opcion == "3":
            dni = int(input("Ingrese el DNI del pasajero: "))
            destino = buscar_destino_por_dni(lista_pasajeros, dni)
            if destino:
                print(f"El pasajero viaja a: {destino}")
            else:
                print("No se encontró un pasajero con ese DNI.")
        elif opcion == "4":
            ciudad = input("Ingrese el nombre de la ciudad: ")
            cantidad = contar_pasajeros_por_ciudad(lista_pasajeros, ciudad)
            print(f"Cantidad de pasajeros que viajan a {ciudad}: {cantidad}")
        elif opcion == "5":
            dni = int(input("Ingrese el DNI del pasajero: "))
            pais = buscar_pais_por_dni(lista_pasajeros, lista_ciudades, dni)
            if pais:
                print(f"El pasajero viaja a: {pais}")
            else:
                print("No se encontró un pasajero con ese DNI.")
        elif opcion == "6":
            pais = input("Ingrese el nombre del país: ")
            cantidad = contar_pasajeros_por_pais(lista_pasajeros, lista_ciudades, pais)
            print(f"Cantidad de pasajeros que viajan a {pais}: {cantidad}")
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
