# Solicitar al usuario que ingrese un día de la semana
dia_semana = input("Ingrese un día de la semana: ").lower()

# Verificar el día de la semana e imprimir un mensaje según corresponda
if dia_semana == "lunes":
    print("Es lunes. ¡Ánimo, comienza una nueva semana!")
elif dia_semana == "viernes":
    print("Es viernes. ¡Feliz viernes, el fin de semana está cerca!")
elif dia_semana == "sábado" or dia_semana == "domingo":
    print("Es fin de semana. ¡Disfruta tu descanso!")
else:
    print("No es lunes, viernes, sábado ni domingo.")
