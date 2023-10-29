class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("Contacto agregado con éxito.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for i, contacto in enumerate(self.contactos, 1):
                print(f"{i}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return
        print(f"Contacto '{nombre}' no encontrado en la agenda.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print("Contacto editado con éxito.")
                return
        print(f"Contacto '{nombre}' no encontrado en la agenda.")

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú de la Agenda:")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    return input("Elija una opción: ")

agenda = Agenda()

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        email = input("Email del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        agenda.agregar_contacto(nuevo_contacto)
    elif opcion == "2":
        agenda.mostrar_contactos()
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        agenda.buscar_contacto(nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto que desea editar: ")
        nuevo_telefono = input("Nuevo teléfono: ")
        nuevo_email = input("Nuevo email: ")
        agenda.editar_contacto(nombre, nuevo_telefono, nuevo_email)
    elif opcion == "5":
        print("Agenda cerrada. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
