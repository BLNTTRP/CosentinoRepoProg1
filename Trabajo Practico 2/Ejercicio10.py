def calcular_precio_entrada(edad):
    if edad < 4:
        return 0  # Menores de 4 años entran gratis
    elif 4 <= edad <= 18:
        return 500  # Edades entre 4 y 18 años pagan $500
    else:
        return 1000  # Mayores de 18 años pagan $1000

# Solicitar la edad del cliente
edad_cliente = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada
precio_entrada = calcular_precio_entrada(edad_cliente)

# Mostrar el precio de la entrada
if precio_entrada == 0:
    print("El cliente puede entrar gratis.")
else:
    print(f"El precio de la entrada es: ${precio_entrada}")
