"""
DESAFIO DA SEMANA 1 - Filtrar Números Pares

PROBLEMA:
Criar um programa que recebe uma lista de números e cria uma NOVA lista
contendo apenas os números pares.

Este é o "Desafio 1" citado no README do repositório — o primeiro dos
três desafios que você vai conseguir resolver ao final do programa.

EXEMPLO:
Entrada: numeros = [1, 2, 3, 4, 5, 6]
Saída esperada: [2, 4, 6]

DICAS:
1. Crie uma lista vazia para guardar os resultados: pares = []
2. Use um "for" para percorrer a lista de entrada
3. Dentro do for, use "if" para testar se o número é par (numero % 2 == 0)
4. Se for par, adicione na lista nova com pares.append(numero)
5. No final, imprima a lista "pares"
"""

# ESCREVA SEU CÓDIGO AQUI
# numeros = [1, 2, 3, 4, 5, 6]

# ↓ COMPLETE ABAIXO ↓
numeros = [1, 2, 3, 4, 5, 6]

pares = []

for lista_pares in numeros:
    if lista_pares % 2 == 0:
        pares.append(lista_pares)

print(pares)