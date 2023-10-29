def ordenamiento_burbuja(lista):
    n = len(lista)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Solicitar al usuario una lista de números
entrada = input("Ingrese una lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

# Aplicar el ordenamiento de burbuja
ordenamiento_burbuja(numeros)

# Mostrar la lista ordenada
print("Lista ordenada en orden ascendente:", numeros)
