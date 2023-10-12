def mostrar_menu_ingredientes(opcion):
    if opcion == "V":
        print("Ingredientes vegetarianos disponibles:")
        print("1. Pimiento")
        print("2. Tofu")
    elif opcion == "NV":
        print("Ingredientes no vegetarianos disponibles:")
        print("1. Peperoni")
        print("2. Jamón")
        print("3. Salmón")
    else:
        print("Opción no válida")

# Solicitar al usuario que elija el tipo de pizza
tipo_pizza = input("¿Qué tipo de pizza desea? (V: Vegetariana, NV: No vegetariana): ").upper()

# Mostrar el menú de ingredientes según la elección
mostrar_menu_ingredientes(tipo_pizza)

# Solicitar al usuario que elija un ingrediente
ingrediente_elegido = input("Seleccione un ingrediente (indique el número): ")

# Asignar el nombre del ingrediente según la elección
if tipo_pizza == "V":
    if ingrediente_elegido == "1":
        ingrediente = "Pimiento"
    elif ingrediente_elegido == "2":
        ingrediente = "Tofu"
    else:
        ingrediente = "Opción no válida"
elif tipo_pizza == "NV":
    if ingrediente_elegido == "1":
        ingrediente = "Peperoni"
    elif ingrediente_elegido == "2":
        ingrediente = "Jamón"
    elif ingrediente_elegido == "3":
        ingrediente = "Salmón"
    else:
        ingrediente = "Opción no válida"
else:
    ingrediente = "Opción no válida"

# Mostrar el tipo de pizza y los ingredientes
print("Tipo de pizza:", "Vegetariana" if tipo_pizza == "V" else "No vegetariana")
print("Ingredientes:", "Mozzarella, Tomate, " + ingrediente)
