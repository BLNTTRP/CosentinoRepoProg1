# Paso 1: Solicitar al usuario que ingrese números en una lista
numeros = []
while True:
    num = int(input("Ingrese un número (o 0 para finalizar): "))
    if num == 0:
        break
    numeros.append(num)

# Paso 2: Solicitar al usuario que ingrese un número para eliminar su primera ocurrencia
num_eliminar = int(input("Ingrese un número a eliminar: "))
if num_eliminar in numeros:
    numeros.remove(num_eliminar)
    print(f"Se ha eliminado la primera ocurrencia de {num_eliminar}.")
else:
    print(f"No se encontró el número {num_eliminar} en la lista.")

# Paso 3: Imprimir la sumatoria de todos los números en la lista
sumatoria = sum(numeros)
print(f"La sumatoria de los números en la lista es: {sumatoria}")

# Paso 4: Solicitar al usuario que ingrese otro número para filtrar la lista original
num_filtrar = int(input("Ingrese un número para filtrar la lista: "))
lista_filtrada = [num for num in numeros if num < num_filtrar]
print("Lista filtrada con números menores que", num_filtrar)
for num in lista_filtrada:
    print(num, end=" ")

# Paso 5: Generar una nueva lista con tuplas (número, cantidad de veces)
conteo_numeros = [(num, numeros.count(num)) for num in numeros]
# Eliminamos duplicados manteniendo el orden de aparición
conteo_numeros = list(dict.fromkeys(conteo_numeros))
print("\nNueva lista con tuplas (número, cantidad de veces):")
for num, cantidad in conteo_numeros:
    print(f"({num},{cantidad})", end=" ")
