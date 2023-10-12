año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("Es año bisiesto.")
else:
    print("No es año bisiesto.")