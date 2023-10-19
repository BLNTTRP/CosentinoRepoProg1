def aplicar_funcion_a_lista(funcion, lista):
    resultados = [funcion(elemento) for elemento in lista]
    return resultados

# Definimos una función que eleva un número al cuadrado
def cuadrado(x):
    return x ** 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicamos la función cuadrado a cada elemento de la lista
resultados = aplicar_funcion_a_lista(cuadrado, numeros)

print(resultados)
