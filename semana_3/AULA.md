# 📘 Semana 3 - Dicionários + Listas de Dicionários

## 🎯 Objetivo da Semana

Até agora você trabalhou com listas de valores soltos (`[50, 150, 80]`).
Mas na vida real, os dados quase sempre têm **nome** — um produto tem preço
E nome E estoque, uma pessoa tem nome E idade E cidade. É pra isso que
existem os **dicionários**.

---

## 1. Criando e Acessando Dicionários

Um dicionário guarda pares de **chave: valor**.

```python
produto = {
    "nome": "Notebook",
    "preco": 3500,
    "estoque": 12
}
```

Você acessa um valor pela sua chave (não por índice numérico como nas listas):

```python
print(produto["nome"])     # Notebook
print(produto["preco"])    # 3500
```

Se a chave pode não existir, use `.get()` (evita erro e permite um valor padrão):

```python
print(produto.get("marca"))          # None (chave não existe)
print(produto.get("marca", "N/A"))   # N/A (valor padrão)
```

---

## 2. Modificando Dicionários

```python
produto["preco"] = 3200          # altera um valor existente
produto["marca"] = "Dell"        # cria uma chave nova
```

---

## 3. Percorrendo Dicionários com `for`

```python
precos = {"produto1": 50, "produto2": 150, "produto3": 100}

for chave in precos:
    print(chave)          # imprime só as chaves: produto1, produto2, produto3

for chave, valor in precos.items():
    print(chave, valor)   # imprime chave e valor juntos
```

- `.items()` é o método mais usado: entrega **chave e valor** ao mesmo tempo,
  igual o `enumerate()` fazia com índice e valor nas listas.
- `.keys()` entrega só as chaves e `.values()` só os valores, caso precise.

---

## 4. Filtrando Dicionários (reaproveitando o padrão FILTRO)

Lembra do padrão filtro da Semana 2 (`lista_nova = []` + `for` + `if` + `append`)?
Ele funciona exatamente igual aqui — só que agora percorrendo `.items()`:

```python
precos = {"produto1": 50, "produto2": 150, "produto3": 100}
caros = []

for nome, preco in precos.items():
    if preco > 100:
        caros.append(nome)

print(caros)  # ['produto2']
```

Esse é o **Desafio 2** do README do repositório: filtrar produtos por preço,
só que retornando os **nomes** (chaves) em vez dos preços.

---

## 5. Listas de Dicionários

O padrão mais poderoso: uma lista onde **cada item é um dicionário** —
ou seja, uma lista de "registros" (como uma tabela).

```python
produtos = [
    {"nome": "Notebook", "tipo": "eletronico", "preco": 3500},
    {"nome": "Mouse", "tipo": "eletronico", "preco": 50},
    {"nome": "Cadeira", "tipo": "moveis", "preco": 800},
]
```

Cada item da lista (`produtos[0]`, `produtos[1]`, ...) é um dicionário completo:

```python
print(produtos[0])              # {'nome': 'Notebook', 'tipo': 'eletronico', 'preco': 3500}
print(produtos[0]["nome"])      # Notebook
```

Para percorrer a lista e acessar os campos de cada produto:

```python
for produto in produtos:
    print(produto["nome"], "-", produto["preco"])
```

### Filtrando com múltiplos critérios

Combinando o padrão filtro com `and`, dá pra filtrar por mais de uma condição:

```python
baratos_eletronicos = []

for produto in produtos:
    if produto["tipo"] == "eletronico" and produto["preco"] < 100:
        baratos_eletronicos.append(produto["nome"])

print(baratos_eletronicos)  # ['Mouse']
```

Essa é a base do **Desafio 3** do README: filtrar uma lista de dicionários
por tipo **e** preço ao mesmo tempo.

---

## 6. Resumo do que você precisa saber para os exercícios

- Criar dicionários com `{"chave": valor}`
- Acessar valores com `dict["chave"]` e `dict.get("chave")`
- Modificar e adicionar chaves
- Percorrer com `for chave, valor in dict.items()`
- Aplicar o padrão filtro em dicionários (retornando as chaves que atendem a condição)
- Criar e percorrer listas de dicionários (`for item in lista: item["chave"]`)
- Combinar múltiplos critérios com `and` dentro do filtro

Agora vá para `exercicios/01_acessar_dicionario.py` e comece a praticar.
