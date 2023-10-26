# Definir el cuadro de goles en un arreglo de dos dimensiones
goles = [
    [0, 4, 2, 1, 3, 0, 5, 2, 4, 1],
    [5, 0, 3, 2, 1, 1, 2, 4, 0, 3],
    [0, 2, 0, 1, 3, 2, 3, 1, 4, 1],
    [1, 0, 2, 0, 0, 0, 3, 1, 2, 0],
    [3, 1, 3, 0, 0, 2, 2, 3, 4, 1],
    [1, 1, 2, 2, 0, 0, 0, 1, 0, 1],
    [0, 2, 0, 3, 2, 3, 0, 1, 2, 2],
    [2, 0, 1, 1, 3, 3, 1, 0, 2, 2],
    [1, 2, 1, 2, 0, 1, 3, 2, 0, 0],
    [4, 0, 4, 0, 1, 1, 1, 2, 2, 0]
]

# Inicializar listas para contar triunfos, empates, derrotas, goles marcados y recibidos
triunfos = [0] * 10
empates = [0] * 10
derrotas = [0] * 10
goles_marcados = [0] * 10
goles_recibidos = [0] * 10

# Calcular resultados de los partidos
for i in range(10):
    for j in range(10):
        if i != j:
            if goles[i][j] > goles[j][i]:
                triunfos[i] += 1
                derrotas[j] += 1
            elif goles[i][j] < goles[j][i]:
                triunfos[j] += 1
                derrotas[i] += 1
            else:
                empates[i] += 1
                empates[j] += 1
            goles_marcados[i] += goles[i][j]
            goles_recibidos[i] += goles[j][i]

# Calcular la diferencia de goles y los puntos obtenidos
diferencia_goles = [g_marcados - g_recibidos for g_marcados, g_recibidos in zip(goles_marcados, goles_recibidos)]
puntos = [triunfos[i] * 3 + empates[i] for i in range(10)]

# Mostrar los resultados para cada equipo
for equipo in range(10):
    print(f"Equipo {equipo + 1}:")
    print(f"Triunfos: {triunfos[equipo]}, Empates: {empates[equipo]}, Derrotas: {derrotas[equipo]}")
    print(f"Diferencia de goles: {diferencia_goles[equipo]}, Puntos: {puntos[equipo]}")
    print()
