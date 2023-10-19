def temperatura_media(temp_max, temp_min):
    return (temp_max + temp_min) / 2

def main():
    # Solicitar al usuario el número de días a ingresar
    num_dias = int(input("Ingrese el número de días: "))

    for dia in range(1, num_dias + 1):
        # Solicitar la temperatura máxima y mínima para el día actual
        temp_max = float(input(f"Temperatura máxima para el día {dia}: "))
        temp_min = float(input(f"Temperatura mínima para el día {dia}: "))

        # Calcular la temperatura media utilizando la función
        temp_media = temperatura_media(temp_max, temp_min)

        # Mostrar la temperatura media para el día actual
        print(f"Temperatura media para el día {dia}: {temp_media}°C")

if __name__ == "__main__":
    main()
