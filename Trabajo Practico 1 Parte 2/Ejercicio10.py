print("Bienvenido, alumno!")
parcial1 = float(input("Ingresa la nota del parcial 1: "))
parcial2 = float(input("Ingresa la nota del parcial 2: "))
parcial3 = float(input("Ingresa la nota del parcial 3: "))
promedio = (parcial1 + parcial2 + parcial3) / 3
examen_final = float(input("Ingresa la nota del examen final: "))
trabajo_final = float(input("Ingresa la nota del trabajo final: "))
nota_final = (promedio * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print("Su nota final de la materia: ", nota_final)