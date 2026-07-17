"""
DESAFIO DA SEMANA 2 - Relatório de Preços

PROBLEMA:
Dada uma lista com os preços de vários produtos, calcule e imprima:
1. A soma total de todos os preços
2. Quantos produtos custam menos que 100 (produtos baratos)
3. Uma nova lista contendo apenas os preços dos produtos baratos

Este desafio combina os TRÊS padrões da AULA.md (acumulador, contador
e filtro) em um único programa — exatamente como você vai precisar
fazer no Desafio 2 do README (mais pra frente, com dicionários).

EXEMPLO:
Entrada: precos = [50, 150, 80, 200, 99, 300]
Saída esperada:
Soma total: 879
Produtos baratos: 3
Lista de baratos: [50, 80, 99]

DICAS:
1. Crie três variáveis antes do for: soma = 0, contador = 0, baratos = []
2. Dentro de UM ÚNICO for, faça as três coisas para cada preço:
   - soma += preco (acumulador)
   - if preco < 100: contador += 1 e baratos.append(preco) (contador + filtro)
3. Depois do for, imprima as três informações
"""

# ESCREVA SEU CÓDIGO AQUI
precos = [50, 150, 80, 200, 99, 300]

# ↓ COMPLETE ABAIXO ↓
soma = 0
baratos = []

for preco in precos:
    soma += preco
    if preco < 100:
        baratos.append(preco)

print(soma)
print(len(baratos))
print(baratos)
