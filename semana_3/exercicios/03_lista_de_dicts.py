"""
EXERCÍCIO 3.3 - Percorrer uma Lista de Dicionários

PROBLEMA:
Dada uma lista de produtos (cada produto é um dicionário com "nome" e
"preco"), imprima uma linha para cada produto no formato:
"{nome}: R${preco}"

EXEMPLO:
Entrada:
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 150},
]

Saída esperada:
Notebook: R$3500
Mouse: R$50
Teclado: R$150

DICAS:
1. Use for produto in produtos: para percorrer a lista
2. Cada "produto" dentro do loop é um dicionário — acesse com produto["nome"] e produto["preco"]
3. Use f-string para montar a linha: f"{produto['nome']}: R${produto['preco']}"
"""

# ESCREVA SEU CÓDIGO AQUI
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 150},
]

# ↓ COMPLETE ABAIXO ↓
