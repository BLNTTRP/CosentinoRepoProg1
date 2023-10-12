años_compu = int(input("Ingresa la antiguedad de tu computador en años: "))
if años_compu < 0:
    print("Error. Valor incorrecto.")
elif años_compu <= 2 and años_compu >= 0:
    print("El computador es nuevo.")
else:
    print("El computador es viejo.")