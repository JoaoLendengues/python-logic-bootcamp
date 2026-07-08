"""
EXERCÍCIO 4.3 - Função que Filtra um Dicionário (Desafio 2, agora reutilizável)

PROBLEMA:
Crie uma função chamada "filtrar_por_preco" que recebe DOIS parâmetros:
- "precos": um dicionário {nome_produto: preco}
- "limite": um número

A função deve RETORNAR uma lista com os nomes dos produtos cujo preço é
maior que "limite".

Depois, chame a função com o mesmo dicionário mas limites diferentes,
e imprima cada resultado.

EXEMPLO:
precos = {"produto1": 50, "produto2": 150, "produto3": 100}

filtrar_por_preco(precos, 100) -> ["produto2"]
filtrar_por_preco(precos, 40)  -> ["produto1", "produto2", "produto3"]

DICAS:
1. Comece com: def filtrar_por_preco(precos, limite):
2. Dentro da função, use for nome, preco in precos.items():
3. Use if preco > limite: para decidir quem entra
4. Adicione o NOME (não o preço) na lista de resultado com append()
5. Use "return" no final (não print dentro da função!)
"""

# ESCREVA SEU CÓDIGO AQUI
precos = {"produto1": 50, "produto2": 150, "produto3": 100}

# ↓ COMPLETE ABAIXO ↓


# Depois de criar a função, teste com estas chamadas:
# print(filtrar_por_preco(precos, 100))
# print(filtrar_por_preco(precos, 40))
