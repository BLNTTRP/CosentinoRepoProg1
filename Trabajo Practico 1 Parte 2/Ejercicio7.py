def conversion(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

minutos = int(input("Ingresa la cantidad de minutos: "))
horas, minutos_restantes = conversion(minutos)
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")