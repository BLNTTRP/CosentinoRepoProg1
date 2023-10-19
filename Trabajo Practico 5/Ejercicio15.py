def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def main():
    numeros_leidos = 0
    
    while True:
        try:
            numero = int(input("Ingresa un número (o ingresa 0 para salir): "))
            if numero == 0:
                break
            numeros_leidos += 1
            fact = factorial(numero)
            print(f"El factorial de {numero} es {fact}")
        except ValueError:
            print("Ingresa un número entero válido.")
    
    print(f"Total de números leídos: {numeros_leidos}")

if __name__ == "__main__":
    main()
