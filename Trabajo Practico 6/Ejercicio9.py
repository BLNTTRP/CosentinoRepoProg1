import random

def inicializar_tablero(filas, columnas):
    cartas = list(range(1, (filas * columnas) // 2 + 1))
    cartas = cartas * 2
    random.shuffle(cartas)
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    return tablero, cartas

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' | '.join(fila))
        print('-' * (4 * len(fila) - 1))

def mostrar_carta(tablero, fila, columna, carta, cartas_encontradas):
    if (fila, columna) not in cartas_encontradas:
        tablero[fila][columna] = str(carta)

def main():
    filas = 4
    columnas = 4
    tablero, cartas = inicializar_tablero(filas, columnas)
    cartas_encontradas = set()
    pares_encontrados = 0

    while pares_encontrados < filas * columnas // 2:
        imprimir_tablero(tablero)
        fila1 = int(input("Ingrese la fila de la primera carta: ")) - 1
        columna1 = int(input("Ingrese la columna de la primera carta: ")) - 1
        fila2 = int(input("Ingrese la fila de la segunda carta: ")) - 1
        columna2 = int(input("Ingrese la columna de la segunda carta: ")) - 1

        carta1 = cartas[filas * fila1 + columna1]
        carta2 = cartas[filas * fila2 + columna2]

        mostrar_carta(tablero, fila1, columna1, carta1, cartas_encontradas)
        mostrar_carta(tablero, fila2, columna2, carta2, cartas_encontradas)

        imprimir_tablero(tablero)

        if carta1 == carta2:
            pares_encontrados += 1
            print(f'¡Encontraste un par! ({carta1})')
            cartas_encontradas.add((fila1, columna1))
            cartas_encontradas.add((fila2, columna2))
        else:
            print('Las cartas no son iguales. Sigue intentando.')

    print('¡Felicitaciones! Has encontrado todas las parejas.')

if __name__ == '__main__':
    main()
