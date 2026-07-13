"""
EXERCÍCIO 2.2 - Somar Valores de uma Lista

PROBLEMA:
Dada uma lista de números, calcule e imprima a soma de todos os valores
e a média (soma dividida pela quantidade de números).

EXEMPLO:
Entrada: numeros = [10, 20, 30, 40]
Saída esperada:
Soma: 100
Média: 25.0

DICAS:
1. Use o padrão ACUMULADOR: crie "soma = 0" antes do for
2. Dentro do for, faça "soma += numero" a cada volta
3. Depois do for, calcule a média: soma / len(numeros)
4. len(numeros) retorna quantos números tem na lista
"""

# ESCREVA SEU CÓDIGO AQUI
numeros = [10, 20, 30, 40]

# ↓ COMPLETE ABAIXO ↓
soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)
print(soma)
print(media)