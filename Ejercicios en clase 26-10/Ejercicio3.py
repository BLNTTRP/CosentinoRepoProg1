# Inicializamos el diccionario con los socios fundadores
socios = {
    1: {'nombre': 'Amanda Núñez', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True},
    2: {'nombre': 'Bárbara Molina', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True},
    3: {'nombre': 'Lautaro Campos', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True}
}

def informar_cantidad_socios(socios):
    print(f"El club tiene {len(socios)} socios.")

def pagar_cuotas(socios, numero_socio):
    if numero_socio in socios:
        socios[numero_socio]['cuota_al_dia'] = True
        print(f"Socio n°{numero_socio} ha pagado todas las cuotas adeudadas.")
    else:
        print(f"No se encontró al socio n°{numero_socio}.")

def modificar_fecha_ingreso(socios, fecha_original, fecha_nueva):
    for numero_socio, datos in socios.items():
        if datos['fecha_ingreso'] == fecha_original:
            datos['fecha_ingreso'] = fecha_nueva

def dar_de_baja(socios, nombre_apellido):
    for numero_socio, datos in socios.items():
        if datos['nombre'] == nombre_apellido:
            del socios[numero_socio]
            print(f"{nombre_apellido} ha sido dado de baja.")
            return
    print(f"No se encontró a {nombre_apellido}.")

def imprimir_listado_socios(socios):
    print("Listado de Socios:")
    for numero_socio, datos in socios.items():
        cuota_al_dia = "al día" if datos['cuota_al_dia'] else "pendiente"
        print(f"Socio n°{numero_socio}, {datos['nombre']}, ingresó: {datos['fecha_ingreso']}, cuota {cuota_al_dia}")

# Función principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Informar cantidad de socios")
        print("2. Registrar pago de cuotas")
        print("3. Modificar fecha de ingreso")
        print("4. Dar de baja a un socio")
        print("5. Imprimir listado de socios")
        print("6. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            informar_cantidad_socios(socios)
        elif opcion == "2":
            numero_socio = int(input("Ingrese el número de socio que ha pagado todas las cuotas: "))
            pagar_cuotas(socios, numero_socio)
        elif opcion == "3":
            fecha_original = input("Ingrese la fecha de ingreso original a modificar (dd/mm/aaaa): ")
            fecha_nueva = input("Ingrese la nueva fecha de ingreso (dd/mm/aaaa): ")
            modificar_fecha_ingreso(socios, fecha_original, fecha_nueva)
        elif opcion == "4":
            nombre_apellido = input("Ingrese el nombre y apellido del socio a dar de baja: ")
            dar_de_baja(socios, nombre_apellido)
        elif opcion == "5":
            imprimir_listado_socios(socios)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
