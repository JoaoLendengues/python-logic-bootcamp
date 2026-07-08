# ✅ Soluções Comentadas - Semana 2

> **Antes de ler:** você já tentou o exercício sozinho pelo menos uma vez?
> Se não, volte e tente. Olhar a solução antes de tentar é o erro #1 do GUIA_ESTUDOS.md.

---

## Exercício 01 - Listar Pares Com Índice

```python
numeros = [5, 2, 7, 4, 9, 6]

for indice, numero in enumerate(numeros):
    if numero % 2 == 0:
        print(f"Índice {indice}: {numero} é par")
```

**Por que funciona:**
- `enumerate(numeros)` entrega, a cada volta do loop, uma dupla `(indice, numero)`.
- `for indice, numero in enumerate(numeros):` "desempacota" essa dupla em duas variáveis de uma vez.
- O `if` dentro do loop filtra: só imprime quando `numero % 2 == 0` (par).
- Sem `enumerate()`, você teria que controlar o índice manualmente com uma variável extra.

---

## Exercício 02 - Somar Valores de uma Lista

```python
numeros = [10, 20, 30, 40]
soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")
```

**Por que funciona:**
- `soma = 0` é o ponto de partida do padrão **acumulador**: antes do loop, o total é zero.
- A cada volta, `soma += numero` (equivalente a `soma = soma + numero`) vai somando o valor atual.
- Depois que o `for` termina (não antes!), `soma` já tem o total de todos os números.
- `soma / len(numeros)` calcula a média: total dividido pela quantidade de itens.

**Erro comum:** calcular `soma / len(numeros)` **dentro** do `for` — isso recalcularia
a média a cada iteração, usando uma soma ainda incompleta. A média só faz sentido
depois que o loop inteiro rodou.

---

## Exercício 03 - Filtrar Produtos Baratos

```python
precos = [50, 150, 80, 200, 99]
baratos = []

for preco in precos:
    if preco < 100:
        baratos.append(preco)

print(baratos)
```

**Por que funciona:**
- Este é o padrão **filtro**, o mesmo do Desafio da Semana 1 — só que aplicado a preços.
- `baratos = []` começa vazia.
- O `if preco < 100` decide quais preços entram na lista nova.
- `baratos.append(preco)` adiciona o preço aprovado no final de `baratos`.

---

## Desafio da Semana - Relatório de Preços

```python
precos = [50, 150, 80, 200, 99, 300]

soma = 0
contador = 0
baratos = []

for preco in precos:
    soma += preco
    if preco < 100:
        contador += 1
        baratos.append(preco)

print(f"Soma total: {soma}")
print(f"Produtos baratos: {contador}")
print(f"Lista de baratos: {baratos}")
```

**Por que funciona:**
- As três variáveis (`soma`, `contador`, `baratos`) são criadas **antes** do `for`,
  cada uma no seu "estado zero" (`0`, `0`, `[]`).
- Dentro de um **único** `for`, cada preço passa pelas três operações:
  - `soma += preco` sempre acontece (acumulador, sem condição).
  - `if preco < 100:` decide se o preço é barato.
  - Se for barato, o `contador += 1` (contador) **e** `baratos.append(preco)` (filtro)
    acontecem juntos, porque estão no mesmo bloco `if`.
- Repare que você não precisa de três loops separados — um só `for` resolve tudo,
  desde que cada padrão seja aplicado corretamente dentro dele.

**Por que isso importa:** essa é a mesma estrutura que você vai usar no Desafio 2
do README, só que na Semana 3 os preços vão estar dentro de um **dicionário**
(`{'produto1': 50, 'produto2': 150, ...}`) em vez de uma lista simples.
