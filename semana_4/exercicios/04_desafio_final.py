"""
DESAFIO FINAL - Os 3 Desafios do README, Como Funções Reutilizáveis

PROBLEMA:
Este é o desafio que fecha o programa. Você vai escrever, em um único
arquivo, as três funções que resolvem os três desafios originais do
README — usando tudo que aprendeu nas 4 semanas.

1. filtrar_pares(numeros)
   - Recebe uma lista de números
   - Retorna uma nova lista só com os pares

2. filtrar_por_preco(precos, limite)
   - Recebe um dicionário {nome: preco} e um número "limite"
   - Retorna uma lista com os nomes dos produtos com preco > limite

3. filtrar_produtos(produtos, tipo, preco_max)
   - Recebe uma lista de dicionários (cada um com "nome", "tipo", "preco")
   - Retorna uma lista com os nomes dos produtos cujo "tipo" é igual ao
     parâmetro "tipo" E cujo "preco" é menor que "preco_max"

EXEMPLO (com os dados de teste já escritos no final do arquivo):

filtrar_pares([1, 2, 3, 4, 5, 6])
-> [2, 4, 6]

filtrar_por_preco({"produto1": 50, "produto2": 150, "produto3": 100}, 100)
-> ["produto2"]

filtrar_produtos(produtos, "eletronico", 100)
-> ["Mouse", "Fone"]

DICAS:
1. Cada função usa o padrão FILTRO: lista vazia, for, if, append, return
2. filtrar_pares: use numero % 2 == 0
3. filtrar_por_preco: percorra com precos.items() e guarde o NOME (chave)
4. filtrar_produtos: combine dois critérios com "and" dentro do if
5. Não use print() dentro das funções — só return. O print fica nos testes no final
"""

# ESCREVA SUAS FUNÇÕES AQUI

# ↓ COMPLETE ABAIXO ↓


# ------------------------------------------------------------------
# TESTES - não precisa mexer aqui, só rodar o arquivo depois de
# escrever as três funções acima
# ------------------------------------------------------------------

print("--- Desafio 1: filtrar_pares ---")
print(filtrar_pares([1, 2, 3, 4, 5, 6]))

print("--- Desafio 2: filtrar_por_preco ---")
precos = {"produto1": 50, "produto2": 150, "produto3": 100}
print(filtrar_por_preco(precos, 100))

print("--- Desafio 3: filtrar_produtos ---")
produtos = [
    {"nome": "Notebook", "tipo": "eletronico", "preco": 3500},
    {"nome": "Mouse", "tipo": "eletronico", "preco": 50},
    {"nome": "Cadeira", "tipo": "moveis", "preco": 800},
    {"nome": "Fone", "tipo": "eletronico", "preco": 80},
]
print(filtrar_produtos(produtos, "eletronico", 100))
