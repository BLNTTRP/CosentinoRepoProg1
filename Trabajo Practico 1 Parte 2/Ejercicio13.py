def invertir_numero(num):
    if num < 10 or num > 99:
        print("El número debe tener 2 cifras.")
        return None
    
    # Obtenemos las unidades y las decenas
    unidades = num % 10
    decenas = num // 10

    # Invertimos el número
    numero_invertido = unidades * 10 + decenas

    return numero_invertido

# -------------------------------------------------

num = int(input("Ingresa un numero de 2 cifras: "))
numero_invertido = invertir_numero(num)
if numero_invertido is not None:
    print(f"El número invertido de {num} es: {numero_invertido}")