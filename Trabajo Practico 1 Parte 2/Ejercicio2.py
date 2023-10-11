import math

cat1 = float(input("Ingresa el cateto 1: "))
cat2 = float(input("Ingresa el cateto 2: "))
hipotenusa = math.sqrt((cat1**2) + (cat2**2))
print("La longitud de la hipotenusa es ", hipotenusa)