def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

def contar_ocurrencias(numero, digito):
    digito_str = str(digito)
    return str(numero).count(digito_str)

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def main():
    mayor_primo = 0
    
    while True:
        try:
            numero = int(input("Ingresa un número primo (o un número no primo para salir): "))
            if not es_primo(numero):
                break
            mayor_primo = max(mayor_primo, numero)
            
            suma = suma_digitos(numero)
            
            print(f"Suma de dígitos del número: {suma}")
            
            digito = int(input("Ingresa un dígito para contar sus ocurrencias: "))
            frecuencia = contar_ocurrencias(numero, digito)
            
            print(f"El dígito {digito} aparece {frecuencia} veces en el número.")
        except ValueError:
            print("Ingresa un número entero válido.")
    
    if mayor_primo != 0:
        fact = factorial(mayor_primo)
        print(f"El factorial del mayor número primo ingresado ({mayor_primo}) es {fact}")
    else:
        print("No se ingresaron números primos.")

if __name__ == "__main__":
    main()
