"""
EXERCÍCIO 2.1 - Listar Pares Com Índice

PROBLEMA:
Dada uma lista de números, percorra a lista e imprima apenas os números
pares, mostrando também a posição (índice) deles na lista original.

Formato da saída: "Índice {indice}: {numero} é par"

EXEMPLO:
Entrada: numeros = [5, 2, 7, 4, 9, 6]
Saída esperada:
Índice 1: 2 é par
Índice 3: 4 é par
Índice 5: 6 é par

DICAS:
1. Use enumerate(numeros) para obter índice E valor ao mesmo tempo
2. for indice, numero in enumerate(numeros):
3. Dentro do for, use if para testar se numero é par (numero % 2 == 0)
4. Use f-string para montar a mensagem: f"Índice {indice}: {numero} é par"
"""

# ESCREVA SEU CÓDIGO AQUI
numeros = [5, 2, 7, 4, 9, 6]

# ↓ COMPLETE ABAIXO ↓
pares = []

for indice, numero in enumerate(numeros):
    if numero % 2 == 0:
        pares.append(numero)
        print(f'Índice {indice}: {numero} é par.')