"""
DESAFIO DA SEMANA 3 - Filtrar com Múltiplos Critérios (prévia do Desafio 3)

PROBLEMA:
Dada uma lista de produtos (cada um é um dicionário com "nome", "tipo" e
"preco"), crie uma lista com os NOMES dos produtos que são do tipo
"eletronico" E custam menos que 100.

Este exercício é uma prévia do "Desafio 3" do README, que combina filtro
por múltiplos critérios em uma lista de dicionários.

EXEMPLO:
Entrada:
produtos = [
    {"nome": "Notebook", "tipo": "eletronico", "preco": 3500},
    {"nome": "Mouse", "tipo": "eletronico", "preco": 50},
    {"nome": "Cadeira", "tipo": "moveis", "preco": 800},
    {"nome": "Fone", "tipo": "eletronico", "preco": 80},
]

Saída esperada: ["Mouse", "Fone"]

DICAS:
1. Crie "resultado = []" antes do for (padrão filtro)
2. Percorra a lista com for produto in produtos:
3. Use if com "and" para testar os dois critérios ao mesmo tempo:
   if produto["tipo"] == "eletronico" and produto["preco"] < 100:
4. Se os dois forem verdadeiros, adicione o nome: resultado.append(produto["nome"])
5. No final, imprima a lista "resultado"
"""

# ESCREVA SEU CÓDIGO AQUI
produtos = [
    {"nome": "Notebook", "tipo": "eletronico", "preco": 3500},
    {"nome": "Mouse", "tipo": "eletronico", "preco": 50},
    {"nome": "Cadeira", "tipo": "moveis", "preco": 800},
    {"nome": "Fone", "tipo": "eletronico", "preco": 80},
]

# ↓ COMPLETE ABAIXO ↓
