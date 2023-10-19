def aplicar_descuento(carrito, descuentos):
    precio_total = 0
    
    for producto, precio in carrito.items():
        if producto in descuentos:
            descuento = descuentos[producto]
            precio_con_descuento = precio * (1 - descuento / 100)
            precio_total += precio_con_descuento
        else:
            precio_total += precio
    
    return precio_total

# Ejemplo de uso:
carrito_de_compra = {
    'producto1': 50,
    'producto2': 30,
    'producto3': 25
}

descuentos = {
    'producto1': 10,
    'producto3': 15
}

precio_final = aplicar_descuento(carrito_de_compra, descuentos)
print(f'Precio final de la compra: ${precio_final:.2f}')
