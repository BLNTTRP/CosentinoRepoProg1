import math

def modulo_vector(vector):
    suma_cuadrados = sum(componente ** 2 for componente in vector)
    modulo = math.sqrt(suma_cuadrados)
    return modulo

# Ejemplo de uso:
vector_3d = (3, 4, 5)
modulo = modulo_vector(vector_3d)
print(f"El módulo del vector {vector_3d} es {modulo:.2f}")
