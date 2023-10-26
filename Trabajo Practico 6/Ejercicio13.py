# Definir el diccionario de precios de frutas
precios_frutas = {
    'manzana': 2.0,
    'banana': 1.0,
    'naranja': 1.5,
    'uva': 3.0,
    'pera': 2.5
}

# Solicitar al usuario una fruta y la cantidad de kilos
fruta = input("Ingrese el nombre de una fruta: ").lower()
kilos = float(input(f"Ingrese la cantidad de kilos de {fruta}: "))

# Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"{kilos} kilos de {fruta} cuestan ${precio_total:.2f}")
else:
    print("La fruta no está en el diccionario.")
