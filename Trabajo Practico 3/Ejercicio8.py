altura = int(input("Ingrese la altura del triángulo: "))

for i in range(1, altura + 1):
    for j in range(2 * i - 1, 0, -2):
        print(j, end=' ')
    print()
