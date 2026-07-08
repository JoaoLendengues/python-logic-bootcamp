"""
EXERCÍCIO 3.1 - Acessar Valores de um Dicionário

PROBLEMA:
Dado um dicionário representando um produto (com "nome", "preco" e
"estoque"), imprima uma frase no formato:
"{nome} custa R${preco} e tem {estoque} unidades em estoque"

EXEMPLO:
Entrada: produto = {"nome": "Notebook", "preco": 3500, "estoque": 12}
Saída esperada: "Notebook custa R$3500 e tem 12 unidades em estoque"

DICAS:
1. Acesse cada valor pela chave: produto["nome"], produto["preco"], produto["estoque"]
2. Use uma f-string para montar a frase:
   f"{produto['nome']} custa R${produto['preco']} e tem {produto['estoque']} unidades em estoque"
"""

# ESCREVA SEU CÓDIGO AQUI
produto = {"nome": "Notebook", "preco": 3500, "estoque": 12}

# ↓ COMPLETE ABAIXO ↓
