def ordenamiento_seleccion(lista):
    n = len(lista)
    
    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Solicitar al usuario una lista de palabras
entrada = input("Ingrese una lista de palabras separadas por espacios: ")
palabras = entrada.split()

# Aplicar el ordenamiento de selección
ordenamiento_seleccion(palabras)

# Mostrar la lista ordenada alfabéticamente
print("Lista ordenada alfabéticamente en orden ascendente:", palabras)
