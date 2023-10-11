print("Bienvenido, vendedor!")
sueldo_base = int(input("Ingrese su sueldo base: $"))
comision = sueldo_base * 0.1
cantidad_ventas = int(input("Ingrese su cantidad de ventas del mes: "))
sueldo_neto = sueldo_base + (comision * cantidad_ventas)
print("Dinero obtenido por concepto de comisiones de ventas: $", (comision * cantidad_ventas))
print("Su sueldo neto final es de $", sueldo_neto)