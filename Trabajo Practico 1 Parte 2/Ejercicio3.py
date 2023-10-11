num1 = int(input("Ingresa el 1er numero: "))
num2 = int(input("Ingresa el 2do numero: "))

suma = num1 + num2  # Suma

if num1 > num2:             # Resta y Division
    resta = num1 - num2
    division = num1 / num2
else:
    resta = num2 - num1
    division = num2 / num1

multiplicacion = num1 * num2    # Multiplicacion

print("La suma de los numeros es ", suma)
print("La resta de los numeros es ", resta)
print("La multiplicacion de los numeros es ", multiplicacion)
print("La division de los numeros es ", division)
