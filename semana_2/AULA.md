# 📘 Semana 2 - Listas + Loops Combinados

## 🎯 Objetivo da Semana

Na Semana 1 você aprendeu a decidir (`if`) e a repetir (`for`). Agora vamos
aplicar as duas coisas em cima de **listas**, que é onde a maioria dos
problemas reais de lógica de programação acontece.

---

## 1. Criando e Acessando Listas

```python
numeros = [10, 20, 30, 40, 50]
```

- Cada item tem uma **posição** (índice), começando em `0`.
- `numeros[0]` → `10` (primeiro item)
- `numeros[-1]` → `50` (último item, sem precisar saber o tamanho)
- `len(numeros)` → `5` (quantidade de itens)

```python
print(numeros[0])   # 10
print(numeros[2])   # 30
print(numeros[-1])  # 50
print(len(numeros)) # 5
```

---

## 2. Modificando Listas

Listas são **mutáveis** — você pode alterá-las depois de criadas.

```python
frutas = ["maçã", "banana"]

frutas.append("laranja")   # adiciona no final -> ["maçã", "banana", "laranja"]
frutas.remove("banana")    # remove o item -> ["maçã", "laranja"]
frutas[0] = "uva"           # substitui pelo índice -> ["uva", "laranja"]
```

`append()` é o método mais importante desta semana: é como você constrói
uma lista nova item por item dentro de um loop.

---

## 3. Percorrendo Listas com `for`

Você já viu isso na Semana 1, mas agora vamos usar mais:

```python
numeros = [10, 20, 30]

for numero in numeros:
    print(numero)
```

Às vezes você precisa também do **índice** de cada item. Para isso existe `enumerate()`:

```python
numeros = [10, 20, 30]

for indice, numero in enumerate(numeros):
    print(f"Índice {indice}: valor {numero}")

# Índice 0: valor 10
# Índice 1: valor 20
# Índice 2: valor 30
```

---

## 4. Três Padrões Que Você Vai Usar o Resto da Vida

### Padrão ACUMULADOR (somar valores)

```python
numeros = [10, 20, 30]
soma = 0

for numero in numeros:
    soma = soma + numero   # ou: soma += numero

print(soma)  # 60
```

### Padrão CONTADOR (contar quantos itens satisfazem algo)

```python
numeros = [1, 2, 3, 4, 5, 6]
contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print(contador)  # 3 (existem 3 números pares)
```

### Padrão FILTRO (criar uma lista nova só com o que interessa)

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)  # [2, 4, 6]
```

Repare que os três padrões têm a **mesma estrutura**:

```
1. Cria uma variável "vazia" antes do loop (0, 0 ou [])
2. Percorre a lista com for
3. Dentro do for, atualiza essa variável (soma, contador ou append)
4. Depois do for, usa/imprime o resultado
```

Esses três padrões, sozinhos ou combinados, resolvem praticamente qualquer
exercício desta semana — e é exatamente assim que o **Desafio 2** do README
(filtrar produtos por preço) vai funcionar.

---

## 5. Resumo do que você precisa saber para os exercícios

- Acessar itens por índice (`lista[0]`, `lista[-1]`)
- Usar `len()` para saber o tamanho da lista
- Adicionar itens com `append()`
- Percorrer listas com `for` e, quando precisar do índice, com `enumerate()`
- Aplicar o padrão **acumulador** para somar valores
- Aplicar o padrão **contador** para contar itens que satisfazem uma condição
- Aplicar o padrão **filtro** para criar uma lista nova a partir de uma condição

Agora vá para `exercicios/01_listar_pares.py` e comece a praticar.
