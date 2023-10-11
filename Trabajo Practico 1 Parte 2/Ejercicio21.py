km_litro = float(input("Ingresa la cantidad de kilometros que puede recorrer con 1 litro: "))
capacidad_tanque = float(input("Ingresa la capacidad total del tanque, en litros: "))
km_a_recorrer = float(input("Ingresa la cantidad de kilometros a recorrer: "))
litros_necesarios = km_a_recorrer / km_litro
tanques_necesarios = litros_necesarios / capacidad_tanque
print(f"Cantidad de tanques de combustible necesarios: {tanques_necesarios}")