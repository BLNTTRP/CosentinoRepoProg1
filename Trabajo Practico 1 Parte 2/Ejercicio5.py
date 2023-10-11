# A = input(nombre, "¿Cuál es tu canción favorita?")

nombre = input("Ingresa tu nombre: ")
mensaje = "Hola " + nombre + "!, ¿Cuál es tu canción favorita?: "
cancion_favorita = input(mensaje)

# precio = input("Precio: ")
# total = precio + (precio * 0.1)

precio = float(input("Precio: "))
total = precio + (precio * 0.1)

# edad = int(input("Edad: "))
# print(tu edad es, edad)

edad = int(input("Edad: "))
print("Tu edad es ", edad)

# edad = int(input("Edad: "))
# print("Veamos si tu edad es 18...", edad=18)

edad = int(input("Edad: "))
print("Veamos si tu edad es 18...")
if edad == 18:
    print("Tienes ", edad, " años.")
else:
    print("No tienes 18 años. Tienes ", edad)