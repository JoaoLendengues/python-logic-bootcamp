"""
EXERCÍCIO 2.3 - Filtrar Produtos Baratos

PROBLEMA:
Dada uma lista com os preços de vários produtos, crie uma NOVA lista
contendo apenas os preços menores que 100 (produtos "baratos").

EXEMPLO:
Entrada: precos = [50, 150, 80, 200, 99]
Saída esperada: [50, 80, 99]

DICAS:
1. Use o padrão FILTRO: crie "baratos = []" antes do for
2. Percorra a lista "precos" com for
3. Use if para testar se o preço é menor que 100 (preco < 100)
4. Se for, adicione na lista nova com baratos.append(preco)
5. No final, imprima a lista "baratos"
"""

# ESCREVA SEU CÓDIGO AQUI
precos = [50, 150, 80, 200, 99]

# ↓ COMPLETE ABAIXO ↓
baratos = []

for lista in precos:
    if lista < 100:
        baratos.append(lista)
print(baratos)