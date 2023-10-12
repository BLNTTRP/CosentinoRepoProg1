voto = input("Elija un candidato por cual votar (A - B - C): ")
voto = voto.upper()
if voto == "A":
    print("Votaste por el partido rojo.")
elif voto == "B":
    print("Votaste por el partido verde.")
elif voto == "C":
    print("Votaste por el partido azul.")
else:
    print("Opción erronea.")