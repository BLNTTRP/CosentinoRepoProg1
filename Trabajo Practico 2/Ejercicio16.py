def suma(a, b):
    return a + b

def multiplicacion(a, b):
    return a * b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b

# Solicitar al usuario los valores y la operación a realizar
a = float(input("Ingrese el primer valor (a): "))
b = float(input("Ingrese el segundo valor (b): "))
operacion = int(input("Seleccione la operación a realizar:\n1. Suma\n2. Multiplicación\n3. Resta\n4. División\n"))

# Realizar la operación según la opción elegida
if operacion == 1:
    resultado = suma(a, b)
    print("El resultado de la suma es:", resultado)
elif operacion == 2:
    resultado = multiplicacion(a, b)
    print("El resultado de la multiplicación es:", resultado)
elif operacion == 3:
    resultado = resta(a, b)
    print("El resultado de la resta es:", resultado)
elif operacion == 4:
    resultado = division(a, b)
    print("El resultado de la división es:", resultado)
else:
    print("Opción no válida. Por favor, elija una operación válida (1-4).")
