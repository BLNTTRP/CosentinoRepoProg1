def calcular_saldo(bitacora):
    saldo = 0

    for operacion in bitacora:
        tipo, cantidad = operacion.split()
        cantidad = int(cantidad)

        if tipo == 'D':
            saldo += cantidad
        elif tipo == 'R':
            saldo -= cantidad

    return saldo

# Inicializar la bitácora y solicitar las operaciones
bitacora = []

print("Introduzca las operaciones (D para depósito, R para retiro, línea vacía para finalizar):")

while True:
    operacion = input()
    if operacion == '':
        break
    bitacora.append(operacion)

# Calcular el saldo final e imprimirlo
saldo_final = calcular_saldo(bitacora)
print("El saldo final es:", saldo_final)
