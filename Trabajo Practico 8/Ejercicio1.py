def contar_digitos(n):
    if n < 0:
        return "El número no es positivo"
    elif n == 0:
        return 1
    else:
        return len(str(n))

# Solicitar al usuario un número positivo
numero = int(input("Ingrese un número positivo: "))

# Calcular y mostrar la cantidad de dígitos
cantidad_digitos = contar_digitos(numero)
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
