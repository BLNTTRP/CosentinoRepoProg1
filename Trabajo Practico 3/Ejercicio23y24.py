total_pagar = 0

while True:
    monto = float(input("Ingrese el monto de la compra (o 0 para terminar): "))

    if monto == 0:
        break
    elif monto < 0:
        print("No se pueden ingresar montos negativos. Intente de nuevo.")
        continue

    total_pagar += monto

if total_pagar > 1000:
    descuento = total_pagar * 0.10
    total_pagar_con_descuento = total_pagar - descuento
    print(f"Total a pagar con un 10% de descuento: ${total_pagar_con_descuento:.2f}")
else:
    print(f"Total a pagar: ${total_pagar:.2f}")

