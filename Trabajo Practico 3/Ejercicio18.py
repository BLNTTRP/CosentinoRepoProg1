def fibonacci(n):
    if n <= 0:
        return "El número debe ser positivo."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence[:n]

# Mostrar los primeros 10 números de la sucesión de Fibonacci
primeros_10_fibonacci = fibonacci(10)
print("Los primeros 10 números de la sucesión de Fibonacci:")
print(primeros_10_fibonacci)
