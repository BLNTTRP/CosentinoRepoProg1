def isMutant(dna):
    rows = len(dna)
    cols = len(dna[0])

    if rows != 6 or cols != 6:
        return False  # No cumple con la matriz de 6x6

    countMutantSequences = 0

    # Verificar secuencias horizontales
    for i in range(rows):
        for j in range(cols - 3):
            sequence = dna[i][j:j+4]
            if any(seq in sequence for seq in ["AAAA", "TTTT", "CCCC", "GGGG"]):
                countMutantSequences += 1

    # Verificar secuencias verticales
    for i in range(rows - 3):
        for j in range(cols):
            sequence = ''.join(dna[k][j] for k in range(i, i+4))
            if any(seq in sequence for seq in ["AAAA", "TTTT", "CCCC", "GGGG"]):
                countMutantSequences += 1

    # Verificar secuencias oblicuas
    for i in range(rows - 3):
        for j in range(cols - 3):
            sequence = ''.join(dna[i+k][j+k] for k in range(4))
            if any(seq in sequence for seq in ["AAAA", "TTTT", "CCCC", "GGGG"]):
                countMutantSequences += 1

    return countMutantSequences > 1  # Si se encuentran más de una secuencia, es mutante.

# Solicitar al usuario las filas del ADN
dna = []
print("Ingrese las filas del ADN (6 filas de 6 letras cada una):")
for i in range(6):
    row = input(f"Fila {i + 1}: ").upper()
    if len(row) != 6 or any(base not in "ATCG" for base in row):
        print("Entrada inválida. Cada fila debe contener 6 letras de 'A', 'T', 'C' o 'G'.")
        exit(1)
    dna.append(row)

result = isMutant(dna)
print("Es mutante" if result else "No es mutante")
