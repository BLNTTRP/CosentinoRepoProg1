numero = int(input("Ingrese un número entero positivo: "))

# Asegurarse de que el número sea positivo
if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    cuenta_atras = ', '.join(str(i) for i in range(numero, -1, -1))
    print(f"Cuenta atrás desde {numero} hasta 0: {cuenta_atras}")
