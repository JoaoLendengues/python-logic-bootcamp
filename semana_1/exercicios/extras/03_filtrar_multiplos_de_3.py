"""
EXTRA 1.3 - Filtrar Múltiplos de 3

PROBLEMA:
Dada uma lista de números, crie uma NOVA lista contendo apenas os
números que são múltiplos de 3.

Esta é uma variação do Desafio da Semana 1 (filtrar pares) — mesma
estrutura, mudando só a condição do "if".

EXEMPLO:
Entrada: numeros = [1, 3, 4, 6, 7, 9, 10, 12]
Saída esperada: [3, 6, 9, 12]

DICAS:
1. Crie uma lista vazia para guardar os resultados: multiplos = []
2. Use um "for" para percorrer a lista de entrada
3. Dentro do for, use "if" para testar se o número é múltiplo de 3
   (dica: um número é múltiplo de 3 quando numero % 3 == 0)
4. Se for múltiplo, adicione na lista nova com multiplos.append(numero)
5. Cuidado com a ordem: é "multiplos.append(numero)", não o contrário
6. No final (fora do for), imprima a lista "multiplos"
"""

# ESCREVA SEU CÓDIGO AQUI
numeros = [1, 3, 4, 6, 7, 9, 10, 12]

# ↓ COMPLETE ABAIXO ↓
