def calcular_fatorial(numero):
    if numero < 0:
        raise ValueError("O número deve ser maior ou igual a zero.")

    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado