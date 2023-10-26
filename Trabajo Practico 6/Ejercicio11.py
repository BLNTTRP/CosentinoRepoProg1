# Definir el diccionario de divisas y símbolos
diccionario_divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Solicitar al usuario una divisa
divisa = input("Ingrese el nombre de una divisa: ")

# Buscar la divisa en el diccionario y mostrar su símbolo o un mensaje de aviso
if divisa in diccionario_divisas:
    simbolo = diccionario_divisas[divisa]
    print(f"El símbolo de {divisa} es {simbolo}.")
else:
    print("La divisa no está en el diccionario.")
