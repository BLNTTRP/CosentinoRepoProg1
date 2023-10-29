def par(n):
    if n == 0:
        return True  # 0 se considera par
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False  # 0 se considera par, por lo que 1 es impar
    else:
        return par(n - 1)

# Ejemplos de uso:
numero = 5
if par(numero):
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")
