# Costo por lápiz en pesos
costo_por_lapiz = 60

# Solicitar al usuario la cantidad de lápices a comprar
cantidad_lapices = int(input("Ingrese la cantidad de lápices a comprar: "))

# Calcular el costo total sin descuento
costo_total = cantidad_lapices * costo_por_lapiz

# Verificar si aplica descuento (1000 o más lápices)
if cantidad_lapices >= 1000:
    descuento = 0.07 * costo_total
    costo_total_con_descuento = costo_total - descuento
    print(f"Costo total con descuento (7%): ${costo_total_con_descuento:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
else:
    print(f"Costo total sin descuento: ${costo_total:.2f}")
