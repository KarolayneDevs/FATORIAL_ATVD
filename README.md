# Projeto de Fatorial em Python

Este projeto foi desenvolvido para uma atividade da disciplina **DevOps Tools**. Nossa equipe ficou responsável pelo tema **fatorial**.

O programa recebe um número inteiro informado pelo usuário e calcula o seu fatorial.

Por exemplo:

```text
5! = 5 × 4 × 3 × 2 × 1

Resultado: 120
```

## Como foi feito

Criamos uma função para realizar o cálculo do fatorial e utilizamos um `for` junto com `range()` para fazer as multiplicações.

Também adicionamos uma verificação para não permitir números negativos.

## Funções e partes do código

* `calcular_fatorial(numero)`: recebe o número informado e realiza o cálculo do fatorial.
* `if numero < 0`: verifica se o número é negativo e impede que o cálculo seja realizado.
* `resultado = 1`: define o valor inicial que será usado nas multiplicações.
* `for i in range(1, numero + 1)`: percorre os números de 1 até o número informado.
* `resultado *= i`: multiplica o resultado pelo número atual do loop.
* `return resultado`: retorna o resultado final do cálculo.
* `input()`: permite que o usuário informe o número.
* `int()`: transforma o valor informado em um número inteiro.
* `print()`: mostra o resultado na tela.
* `try` e `except`: tratam possíveis erros durante a execução do programa.

## Sobre o loop

Uma das preocupações durante o desenvolvimento foi evitar um **loop infinito**.

Para isso, utilizamos o `for` com `range()`, pois a quantidade de repetições fica definida de acordo com o número informado pelo usuário.

Por exemplo, se o número for `5`, o loop percorre:

```text
1 → 2 → 3 → 4 → 5
```

Depois de chegar ao último número, o loop termina automaticamente.

Dessa forma, não precisamos controlar manualmente uma variável de repetição, como aconteceria em um `while`, reduzindo a possibilidade de o programa ficar executando sem parar.

## Testes

Para verificar se o programa estava funcionando corretamente, criamos testes utilizando o **Pytest**.

Foram testados:

* Fatorial de 0;
* Fatorial de 1;
* Fatorial de 5;
* Fatorial de 10;
* Número negativo.

Os 5 testes foram executados com sucesso:

```text
5 passed
```

## Estrutura do projeto

```text
FATORIAL_ATVD/
│
├── app/
│   ├── __init__.py
│   └── fatorial.py
│
├── tests/
│   └── test_fatorial.py
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Tecnologias utilizadas

* Python
* Pytest
* Visual Studio Code
* Git
* GitHub

## Participantes

* Karolayne da Silva Diniz
* Maxwilliam da Silva Sena
* Giovanna Manuella Galucio Crisostomo
* Robson Adroaldo Carvalho Pinheiro
