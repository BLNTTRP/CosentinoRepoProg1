def calcular_solucion(a, b):
    if a == 0:
        if b == 0:
            return "Todos los números son solución."
        else:
            return "La ecuación no tiene solución."
    else:
        solucion = -b / a
        return f"La solución de la ecuación es: x = {solucion}"

# Solicitar al usuario los coeficientes de la ecuación
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

# Calcular la solución de la ecuación
solucion = calcular_solucion(a, b)

# Mostrar la solución
print(solucion)
