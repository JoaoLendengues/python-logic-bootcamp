# ✅ Soluções Comentadas - Semana 4

> **Antes de ler:** você já tentou o exercício sozinho pelo menos uma vez?
> Se não, volte e tente. Olhar a solução antes de tentar é o erro #1 do GUIA_ESTUDOS.md.

---

## Exercício 01 - Sua Primeira Função

```python
def verificar_maior_idade(idade):
    if idade >= 18:
        return "Pode dirigir"
    else:
        return "Não pode dirigir"

print(verificar_maior_idade(25))  # Pode dirigir
print(verificar_maior_idade(15))  # Não pode dirigir
print(verificar_maior_idade(18))  # Pode dirigir
```

**Por que funciona:**
- `def verificar_maior_idade(idade):` cria a função e diz que ela recebe um parâmetro chamado `idade`.
- Cada `return` devolve uma string e **encerra a função imediatamente** — por isso
  não precisamos nos preocupar em "sair" do `if/else`, o `return` já faz isso.
- `print(verificar_maior_idade(25))` primeiro executa a função (que devolve
  `"Pode dirigir"`), e só depois o `print` mostra esse valor devolvido na tela.

---

## Exercício 02 - Função que Filtra uma Lista

```python
def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print(filtrar_pares([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(filtrar_pares([10, 11, 12, 13]))    # [10, 12]
```

**Por que funciona:**
- É o mesmo padrão filtro da Semana 1/2, só que agora embrulhado numa função.
- `numeros` é o parâmetro — a lista muda a cada chamada, mas a lógica interna
  (percorrer e filtrar) continua igual.
- `return pares` devolve a lista pronta. Repare que não tem `print` nenhum
  **dentro** da função — quem decide o que fazer com o resultado é quem chama ela.

---

## Exercício 03 - Função que Filtra um Dicionário

```python
def filtrar_por_preco(precos, limite):
    caros = []
    for nome, preco in precos.items():
        if preco > limite:
            caros.append(nome)
    return caros

precos = {"produto1": 50, "produto2": 150, "produto3": 100}

print(filtrar_por_preco(precos, 100))  # ['produto2']
print(filtrar_por_preco(precos, 40))   # ['produto1', 'produto2', 'produto3']
```

**Por que funciona:**
- Igual ao Desafio 2 da Semana 3, mas agora `limite` é um **parâmetro** em vez
  de um número fixo escrito dentro da função.
- Isso é o que torna a função reutilizável: a mesma função responde
  "quem é mais caro que 100?" e "quem é mais caro que 40?" sem duplicar código.

---

## Desafio Final - Os 3 Desafios do README, Como Funções

```python
def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


def filtrar_por_preco(precos, limite):
    caros = []
    for nome, preco in precos.items():
        if preco > limite:
            caros.append(nome)
    return caros


def filtrar_produtos(produtos, tipo, preco_max):
    resultado = []
    for produto in produtos:
        if produto["tipo"] == tipo and produto["preco"] < preco_max:
            resultado.append(produto["nome"])
    return resultado


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
```

**Saída esperada:**
```
--- Desafio 1: filtrar_pares ---
[2, 4, 6]
--- Desafio 2: filtrar_por_preco ---
['produto2']
--- Desafio 3: filtrar_produtos ---
['Mouse', 'Fone']
```

**Por que funciona:**
- As três funções seguem exatamente o mesmo esqueleto: variável de resultado
  vazia → `for` → `if` (com um ou dois critérios) → `append` → `return`.
- `filtrar_produtos` é a mais complexa: para cada `produto` (um dicionário)
  dentro da lista `produtos`, o `if` testa **dois** critérios com `and`:
  `produto["tipo"] == tipo` e `produto["preco"] < preco_max`. Os dois precisam
  ser verdadeiros para o nome entrar no resultado.
- Nenhuma das três funções usa `print` — elas só calculam e devolvem (`return`).
  Quem decide imprimir é o código de teste no final do arquivo, fora das funções.

**Se você chegou até aqui:** você acabou de resolver, com funções reutilizáveis,
os três desafios que o README prometia lá no início. Da próxima vez que precisar
filtrar uma lista, um dicionário ou uma lista de dicionários, você já sabe o
caminho: variável vazia, `for`, `if`, `append`/`return`.
