from app.fatorial import calcular_fatorial


try:
    numero = int(input("Digite um número inteiro: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}.")
except ValueError as erro:
    print(erro)