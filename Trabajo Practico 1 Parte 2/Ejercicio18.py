monto_cena = float(input("Ingrese el valor de la cena: $"))
adicional_servicio = monto_cena * 0.062
adicional_propina = monto_cena * 0.10
print(f"Cargo por servicio: ${adicional_servicio}")
print(f"Cargo por propina: ${adicional_propina}")
print(f"Monto final a pagar: ${monto_cena + adicional_propina + adicional_servicio}")