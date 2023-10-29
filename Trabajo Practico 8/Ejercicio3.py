def encontrar_posiciones(a, b, start=0):
    # Encontrar la primera posición de b en a a partir de start
    pos = a.find(b, start)
    
    # Si no se encuentra más b en a, regresar una lista vacía
    if pos == -1:
        return []
    
    # Si se encontró una posición, llamar recursivamente para encontrar más
    return [pos] + encontrar_posiciones(a, b, pos + 1)

# Ejemplo de uso:
a = "abracadabraabracadabra"
b = "abra"
posiciones = encontrar_posiciones(a, b)
print("Posiciones de 'abra' en 'abracadabraabracadabra':", posiciones)
