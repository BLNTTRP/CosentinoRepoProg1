def obtener_diagonal_principal(matriz):
    diagonal_principal = []
    for i in range(len(matriz)):
        diagonal_principal.append(matriz[i][i])
    return diagonal_principal

def obtener_diagonal_inversa(matriz):
    diagonal_inversa = []
    for i in range(len(matriz)):
        diagonal_inversa.append(matriz[i][len(matriz) - i - 1])
    return diagonal_inversa

# Ejemplo de matriz cuadrada
matriz_cuadrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_principal = obtener_diagonal_principal(matriz_cuadrada)
diagonal_inversa = obtener_diagonal_inversa(matriz_cuadrada)

print("Diagonal Principal:", diagonal_principal)
print("Diagonal Inversa:", diagonal_inversa)
