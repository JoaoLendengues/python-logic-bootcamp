# 📘 Semana 1 - Condicionais (if/else) + Loops (for)

## 🎯 Objetivo da Semana

Aprender a tomar decisões no código (`if`/`elif`/`else`) e a repetir ações (`for`).
São as duas ferramentas mais usadas em qualquer programa.

---

## 1. Condicionais (`if` / `elif` / `else`)

Um programa quase sempre precisa decidir o que fazer dependendo de uma condição.

```python
idade = 20

if idade >= 18:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
```

- `if` testa uma condição. Se for `True`, executa o bloco indentado.
- `else` executa quando a condição do `if` é `False`.
- `elif` (else if) permite testar mais de uma condição em sequência:

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Insuficiente")
```

**Importante:** o Python testa as condições de cima para baixo e para no primeiro `if`/`elif` que for `True`.

### Operadores de comparação

| Operador | Significado       |
|----------|--------------------|
| `==`     | igual a             |
| `!=`     | diferente de        |
| `>`      | maior que           |
| `<`      | menor que           |
| `>=`     | maior ou igual a    |
| `<=`     | menor ou igual a    |

### Operadores lógicos

```python
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")

if idade < 18 or not tem_carteira:
    print("Não pode dirigir")
```

- `and` → as duas condições precisam ser verdadeiras
- `or` → pelo menos uma condição precisa ser verdadeira
- `not` → inverte o valor (True vira False e vice-versa)

---

## 2. Loops (`for`)

Um `for` repete um bloco de código para cada item de uma sequência.

```python
for numero in range(1, 6):
    print(numero)
# Imprime: 1 2 3 4 5
```

- `range(1, 6)` gera os números de 1 até 5 (o último número, 6, **não** entra).
- `range(5)` gera 0, 1, 2, 3, 4 (começa em 0 por padrão).

Também dá pra percorrer listas diretamente:

```python
numeros = [10, 20, 30]

for numero in numeros:
    print(numero)
```

### Combinando `for` com `if`

Essa combinação é a base de praticamente tudo que você vai construir daqui pra frente:

```python
numeros = [1, 2, 3, 4, 5, 6]

for numero in numeros:
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é ímpar")
```

O operador `%` (módulo/resto da divisão) é a ferramenta clássica para descobrir se um número é par (`numero % 2 == 0`) ou ímpar (`numero % 2 != 0`).

---

## 3. Resumo do que você precisa saber para os exercícios

- Escrever condições com `if` / `elif` / `else`
- Usar os operadores de comparação (`>`, `<`, `>=`, `<=`, `==`, `!=`)
- Combinar condições com `and`, `or`, `not`
- Repetir código com `for` e `range()`
- Percorrer uma lista com `for`
- Usar `%` para saber se um número é par ou ímpar
- Juntar `for` + `if` para filtrar itens de uma lista

Agora vá para `exercicios/01_condicional_basico.py` e comece a praticar.
