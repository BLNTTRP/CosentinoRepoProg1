def contar_ocurrencias(numero, digito):
    # Convierte el número en una cadena para trabajar con los dígitos individualmente
    numero_str = str(numero)
    digito_str = str(digito)
    
    # Inicializa un contador de ocurrencias
    ocurrencias = 0
    
    # Itera a través de los dígitos del número y cuenta las ocurrencias del dígito
    for d in numero_str:
        if d == digito_str:
            ocurrencias += 1
    
    return ocurrencias

def main():
    try:
        numero = int(input("Ingresa un número entero: "))
        digito = int(input("Ingresa un dígito para contar sus ocurrencias: "))
        
        ocurrencias = contar_ocurrencias(numero, digito)
        
        print(f"El dígito {digito} aparece {ocurrencias} veces en el número {numero}.")
    except ValueError:
        print("Ingresa un número entero y un dígito válido.")

if __name__ == "__main__":
    main()
