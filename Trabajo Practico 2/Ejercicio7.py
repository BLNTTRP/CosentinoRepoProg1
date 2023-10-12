num1 = int(input("Ingresa el 1er numero: "))
num2 = int(input("Ingresa el 2do numero: "))
num3 = int(input("Ingresa el 3er numero: "))

mayor = num1
menor = num1

if num2 > mayor:
    mayor = num2
elif num2 < menor:
    menor = num2

if num3 > mayor:
    mayor = num3
elif num3 < menor:
    menor = num3

print(f"El mayor numero ingresado: {mayor}")
print(f"El menor numero ingresado: {menor}")