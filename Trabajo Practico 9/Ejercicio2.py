class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular  # Usamos atributos privados con __ para encapsulación
        self.__cantidad = cantidad

    def set_titular(self, titular):
        if isinstance(titular, str):
            self.__titular = titular
        else:
            print("Error: El titular debe ser una cadena de caracteres.")

    def get_titular(self):
        return self.__titular

    def set_cantidad(self, cantidad):
        if isinstance(cantidad, (int, float)) and cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("Error: La cantidad debe ser un número no negativo.")

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad en la cuenta: ${self.__cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

# Ejemplo de uso:
cuenta1 = Cuenta("Juan Pérez", 1000.0)
cuenta1.mostrar()

cuenta1.ingresar(500.0)
cuenta1.retirar(200.0)

cuenta1.mostrar()
