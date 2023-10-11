def intercambiar_valores(num1, num2):
    aux = num1
    num1 = num2
    num2 = aux
    return num1, num2

num1 = int(input("Ingresa el 1er numero: "))
num2 = int(input("Ingresa el 2do numero: "))
num1, num2 = intercambiar_valores(num1, num2)
print("Variable 1: ", num1)
print("Variable 2: ", num2)