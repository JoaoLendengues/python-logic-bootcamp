"""
EXERCÍCIO 3.2 - Filtrar Produtos por Preço (Desafio 2 do README)

PROBLEMA:
Dado um dicionário onde as chaves são nomes de produtos e os valores são
os preços, crie uma lista com os NOMES dos produtos cujo preço é maior
que 100.

Este é o "Desafio 2" citado no README do repositório.

EXEMPLO:
Entrada: precos = {"produto1": 50, "produto2": 150, "produto3": 100}
Saída esperada: ["produto2"]

(Repare que "produto3" com preço 100 NÃO entra: a condição é maior que 100,
não maior ou igual.)

DICAS:
1. Use o padrão FILTRO: crie "caros = []" antes do for
2. Percorra o dicionário com for nome, preco in precos.items():
3. Use if para testar se o preco é maior que 100 (preco > 100)
4. Se for, adicione o NOME (não o preço) na lista: caros.append(nome)
5. No final, imprima a lista "caros"
"""

# ESCREVA SEU CÓDIGO AQUI
precos = {"produto1": 50, "produto2": 150, "produto3": 100}

# ↓ COMPLETE ABAIXO ↓
