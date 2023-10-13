inicio = int(input("Ingrese el primer número entero: "))
fin = int(input("Ingrese el segundo número entero: "))

print("Números pares:")
for i in range(inicio, fin + 1):
    if i % 2 == 0:
        print(i)

print("\nNúmeros impares:")
for i in range(inicio, fin + 1):
    if i % 2 != 0:
        print(i)
