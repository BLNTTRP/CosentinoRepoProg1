class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtener_lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_de_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# Solicitar al usuario los lados del triángulo
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)

print(f"El lado con mayor longitud es: {triangulo.obtener_lado_mayor()}")
print(f"El triángulo es de tipo: {triangulo.tipo_de_triangulo()}")
