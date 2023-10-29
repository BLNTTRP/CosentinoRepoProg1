def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        palabra_actual = lista[i]
        j = i - 1
        while j >= 0 and len(palabra_actual) < len(lista[j]):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = palabra_actual

# Solicitar al usuario una lista de cadenas
entrada = input("Ingrese una lista de cadenas separadas por espacios: ")
cadenas = entrada.split()

# Aplicar el ordenamiento de inserción por longitud de cadenas
ordenamiento_insercion(cadenas)

# Mostrar la lista de cadenas ordenada por longitud
print("Lista de cadenas ordenada por longitud:")
for cadena in cadenas:
    print(cadena)
