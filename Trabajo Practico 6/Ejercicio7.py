# Inicializamos un diccionario para contar las ocurrencias de cada carácter
ocurrencias = {}

# Procesar 50 strings ingresados por el usuario
for _ in range(50):
    cadena = input("Ingrese un string (o presione Enter para finalizar): ")
    
    if not cadena:
        break
    
    # Contar las ocurrencias de cada carácter en el string
    for caracter in cadena:
        if caracter in ocurrencias:
            ocurrencias[caracter] += 1
        else:
            ocurrencias[caracter] = 1

# Imprimir la cantidad total de ocurrencias de cada carácter
print("Cantidad total de ocurrencias de cada carácter:")
for caracter, cantidad in ocurrencias.items():
    print(f"'{caracter}': {cantidad}")
