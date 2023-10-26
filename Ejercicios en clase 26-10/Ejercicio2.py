def obtener_domicilios_facturacion(ventas):
    domicilios_facturacion = set()  # Usamos un conjunto para evitar duplicados
    
    for venta in ventas:
        cliente, _, _, domicilio = venta
        domicilios_facturacion.add(domicilio)
    
    return list(domicilios_facturacion)

# Ejemplo de uso:
ventas = [
    ('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'),
    ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),
    ('Nuria Costa', 10, 500.0, 'Calle 1 - 456'),
    ('María Pérez', 15, 750.0, 'Calle 3 - 123')
]

domicilios = obtener_domicilios_facturacion(ventas)
print("Domicilios de clientes para enviar la factura de compra:")
for domicilio in domicilios:
    print(domicilio)
