def encontrar_maximo_y_minimo(lista):
    if not lista:
        return None, None  # Retorna None si la lista está vacía
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

def main():
    # Solicitar al usuario que ingrese números separados por espacios
    entrada = input("Ingrese números separados por espacios: ")
    
    # Dividir la entrada en una lista de números
    numeros = [float(numero) for numero in entrada.split()]
    
    # Llamar a la función para encontrar el máximo y mínimo
    maximo, minimo = encontrar_maximo_y_minimo(numeros)
    
    # Mostrar los resultados
    if maximo is not None and minimo is not None:
        print(f"Máximo: {maximo}")
        print(f"Mínimo: {minimo}")
    else:
        print("La lista está vacía.")

if __name__ == "__main__":
    main()
