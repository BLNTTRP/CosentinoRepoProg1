def solicitar_cantidad():
    while True:
        cantidad = float(input("Ingrese la cantidad a ahorrar (objetivo): "))
        if cantidad > 0:
            return cantidad
        else:
            print("La cantidad debe ser positiva. Intente de nuevo.")

objetivo_ahorro = solicitar_cantidad()
total_ahorrado = 0

while total_ahorrado < objetivo_ahorro:
    while True:
        cantidad_ingresada = float(input("Ingrese la cantidad a ahorrar (o 0 para terminar): "))
        if cantidad_ingresada >= 0:
            break
        else:
            print("La cantidad debe ser positiva. Intente de nuevo.")

    if cantidad_ingresada == 0:
        print("Se ha alcanzado el objetivo de ahorro.")
        break

    total_ahorrado += cantidad_ingresada
    print(f"Total ahorrado hasta ahora: {total_ahorrado}")

print("¡Felicidades! Se ha alcanzado o superado el objetivo de ahorro.")
