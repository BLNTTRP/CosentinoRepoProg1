class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre  # Usamos atributos privados con __ para encapsulación
        self.__edad = edad
        self.__dni = dni

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("Error: El nombre debe ser una cadena de caracteres.")

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and 0 <= edad <= 120:  # Suponemos edades entre 0 y 120 años
            self.__edad = edad
        else:
            print("Error: La edad debe ser un entero entre 0 y 120.")

    def get_edad(self):
        return self.__edad

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 8:  # Suponemos DNI de 8 caracteres
            self.__dni = dni
        else:
            print("Error: El DNI debe ser una cadena de 8 caracteres.")

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad} años")
        print(f"DNI: {self.__dni}")

    def esMayorDeEdad(self):
        return self.__edad >= 18

# Ejemplo de uso:
persona1 = Persona("Juan Pérez", 25, "12345678")
persona1.mostrar()
print("¿Es mayor de edad?", persona1.esMayorDeEdad())
