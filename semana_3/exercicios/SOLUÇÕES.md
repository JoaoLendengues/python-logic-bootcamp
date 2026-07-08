# ✅ Soluções Comentadas - Semana 3

> **Antes de ler:** você já tentou o exercício sozinho pelo menos uma vez?
> Se não, volte e tente. Olhar a solução antes de tentar é o erro #1 do GUIA_ESTUDOS.md.

---

## Exercício 01 - Acessar Valores de um Dicionário

```python
produto = {"nome": "Notebook", "preco": 3500, "estoque": 12}

print(f"{produto['nome']} custa R${produto['preco']} e tem {produto['estoque']} unidades em estoque")
```

**Por que funciona:**
- Cada valor do dicionário é acessado pela sua chave: `produto["nome"]`, `produto["preco"]`, `produto["estoque"]`.
- Dentro de uma f-string, usamos aspas simples (`produto['nome']`) porque a f-string
  já está entre aspas duplas — isso evita conflito de aspas.

---

## Exercício 02 - Filtrar Produtos por Preço (Desafio 2)

```python
precos = {"produto1": 50, "produto2": 150, "produto3": 100}
caros = []

for nome, preco in precos.items():
    if preco > 100:
        caros.append(nome)

print(caros)
```

**Por que funciona:**
- `.items()` entrega **chave e valor** juntos a cada volta do loop — aqui chamamos
  a chave de `nome` e o valor de `preco`, porque é isso que eles representam.
- O `if preco > 100` filtra: `produto3` tem preço exatamente `100`, então
  `100 > 100` é `False` e ele **não** entra na lista.
- `caros.append(nome)` guarda o **nome** (a chave), não o preço — é isso que o
  desafio pede: saber *quais* produtos são caros, não seus valores.
- Resultado: `["produto2"]`.

---

## Exercício 03 - Percorrer uma Lista de Dicionários

```python
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 150},
]

for produto in produtos:
    print(f"{produto['nome']}: R${produto['preco']}")
```

**Por que funciona:**
- `produtos` é uma lista; cada item dela é um dicionário completo.
- `for produto in produtos:` faz `produto` valer, a cada volta, **um dicionário
  inteiro** (`{"nome": "Notebook", "preco": 3500}`, depois o próximo, etc).
- Dentro do loop, acessamos os campos desse dicionário normalmente com `produto["nome"]` e `produto["preco"]`.

---

## Desafio da Semana - Filtrar com Múltiplos Critérios

```python
produtos = [
    {"nome": "Notebook", "tipo": "eletronico", "preco": 3500},
    {"nome": "Mouse", "tipo": "eletronico", "preco": 50},
    {"nome": "Cadeira", "tipo": "moveis", "preco": 800},
    {"nome": "Fone", "tipo": "eletronico", "preco": 80},
]

resultado = []

for produto in produtos:
    if produto["tipo"] == "eletronico" and produto["preco"] < 100:
        resultado.append(produto["nome"])

print(resultado)
```

**Por que funciona:**
- Mesmo padrão filtro de sempre: `resultado = []` antes do loop, `for` percorrendo
  a lista, `if` decidindo quem entra, `append()` adicionando.
- A diferença é que agora o `if` testa **duas condições com `and`**:
  `produto["tipo"] == "eletronico"` **e** `produto["preco"] < 100`.
- As duas precisam ser verdadeiras ao mesmo tempo para o produto entrar no resultado.
  "Cadeira" tem preço baixo comparado ao Notebook, mas não é `eletronico`, então
  fica de fora. "Notebook" é eletrônico, mas custa mais que 100, também fica de fora.
- Resultado: `["Mouse", "Fone"]` — os únicos que passam nos dois critérios.

**Por que isso importa:** essa é exatamente a lógica do **Desafio 3** do README.
Se você conseguiu resolver isso, os três desafios originais do programa já
estão ao seu alcance — falta só a Semana 4 (funções) para organizar tudo isso
em blocos reutilizáveis.
