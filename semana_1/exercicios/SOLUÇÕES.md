# ✅ Soluções Comentadas - Semana 1

> **Antes de ler:** você já tentou o exercício sozinho pelo menos uma vez?
> Se não, volte e tente. Olhar a solução antes de tentar é o erro #1 do GUIA_ESTUDOS.md.

---

## Exercício 01 - Condicional Básico

```python
idade = 25

if idade >= 18:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
```

**Por que funciona:**
- `if idade >= 18` testa a condição.
- Se `True` → executa o bloco do `if` (`"Pode dirigir"`).
- Se `False` → executa o bloco do `else` (`"Não pode dirigir"`).
- Com `idade = 25`, a condição é `True`, então imprime `"Pode dirigir"`.

**Teste variações:** troque `idade` por `15`, `18` e `0` e veja se o resultado muda como esperado.

---

## Exercício 02 - Condicional de Preço

```python
preco = 100

if preco < 50:
    print("Barato")
elif preco <= 150:
    print("Médio")
else:
    print("Caro")
```

**Por que funciona:**
- O Python testa as condições em ordem, de cima para baixo.
- Se `preco < 50` for `False`, ele passa para o `elif preco <= 150`.
- Repare que não precisamos escrever `preco >= 50 and preco <= 150`: como o
  primeiro `if` já garantiu que `preco` não é menor que 50, basta checar `<= 150`.
- Se nenhuma das duas for `True`, cai no `else` (`"Caro"`).

**Erro comum:** inverter a ordem (`elif preco > 150` antes de `preco < 50`) também
funciona, mas fica mais fácil de errar a lógica. Comece sempre pelo caso mais simples.

---

## Exercício 03 - Par ou Ímpar em Lista

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
```

**Por que funciona:**
- `for numero in numeros` repete o bloco uma vez para cada item da lista,
  guardando o valor atual na variável `numero`.
- `numero % 2` calcula o resto da divisão por 2. Se o resto é `0`, o número é par.
- O `if/else` roda de novo a cada volta do loop, então cada número é testado individualmente.

---

## Desafio da Semana - Filtrar Números Pares

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
```

**Por que funciona:**
- `pares = []` cria uma lista vazia que vai guardar só os números pares.
- O `for` percorre cada número da lista original.
- O `if` filtra: só entra no bloco quando `numero % 2 == 0` (par).
- `pares.append(numero)` adiciona o número par no final da lista `pares`.
- No fim, `pares` contém `[2, 4, 6]` — exatamente o Desafio 1 do README.

**Por que isso importa:** esse padrão (lista vazia + `for` + `if` + `append`) é
a base dos Desafios 2 e 3 do README, que você vai resolver nas Semanas 2 e 3
usando dicionários no lugar de números simples.
