# 📘 Semana 4 - Funções + Integração de Tudo

## 🎯 Objetivo da Semana

Você já sabe decidir (`if`), repetir (`for`), guardar coleções (listas) e
guardar registros (dicionários). Esta semana você aprende a empacotar tudo
isso em **funções** — blocos de código reutilizáveis, com nome e parâmetros.

É a última peça antes de resolver os três desafios originais do README.

---

## 1. Criando uma Função

```python
def verificar_maior_idade(idade):
    if idade >= 18:
        return "Pode dirigir"
    else:
        return "Não pode dirigir"
```

- `def` começa a definição da função, seguido do **nome** e dos **parâmetros** entre parênteses.
- `idade` é um **parâmetro**: um valor que a função recebe de fora.
- `return` devolve um resultado para quem chamou a função — e **encerra** a função ali.

Para usar a função, você **chama** ela passando um valor:

```python
resultado = verificar_maior_idade(25)
print(resultado)  # Pode dirigir

print(verificar_maior_idade(15))  # Não pode dirigir
```

---

## 2. `return` não é `print`

Esse é o erro mais comum de quem está aprendendo funções.

```python
def dobro_errado(numero):
    print(numero * 2)   # ❌ só mostra na tela, não devolve nada

def dobro_certo(numero):
    return numero * 2   # ✅ devolve o valor para ser usado depois
```

```python
resultado = dobro_errado(5)   # imprime "10" na tela
print(resultado)              # None -> a função não devolveu nada!

resultado = dobro_certo(5)    # não imprime nada sozinha
print(resultado)              # 10 -> o valor foi devolvido e guardado
```

**Regra prática:** use `print()` só quando quiser *mostrar* algo na tela.
Use `return` quando quiser que o resultado possa ser usado em outro lugar
do programa (guardado em uma variável, passado para outra função, etc).

---

## 3. Funções com Mais de Um Parâmetro

```python
def classificar_preco(preco, limite):
    if preco > limite:
        return "Caro"
    else:
        return "Barato"

print(classificar_preco(150, 100))  # Caro
print(classificar_preco(50, 100))   # Barato
```

Parametrizar o `limite` (em vez de deixar `100` fixo dentro da função) é o
que torna a função **reutilizável** para qualquer situação, não só para um caso específico.

---

## 4. Funções que Recebem e Devolvem Listas

Os três padrões da Semana 2 (acumulador, contador, filtro) funcionam
exatamente igual dentro de uma função — a diferença é que agora eles
viram um bloco reutilizável:

```python
def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print(filtrar_pares([1, 2, 3, 4, 5, 6]))   # [2, 4, 6]
print(filtrar_pares([10, 11, 12, 13]))     # [10, 12]
```

Repare: a mesma função funciona para **qualquer** lista de números que
você passar — é isso que significa "reutilizável".

---

## 5. Funções que Recebem Dicionários

```python
def filtrar_por_preco(precos, limite):
    caros = []
    for nome, preco in precos.items():
        if preco > limite:
            caros.append(nome)
    return caros

produtos = {"produto1": 50, "produto2": 150, "produto3": 100}
print(filtrar_por_preco(produtos, 100))  # ['produto2']
print(filtrar_por_preco(produtos, 40))   # ['produto1', 'produto2', 'produto3']
```

Ao transformar `limite` em parâmetro, a mesma função resolve o Desafio 2
do README para **qualquer** valor de corte, não só para `100`.

---

## 6. Juntando Tudo: Funções com Listas de Dicionários

```python
def filtrar_produtos(produtos, tipo, preco_max):
    resultado = []
    for produto in produtos:
        if produto["tipo"] == tipo and produto["preco"] < preco_max:
            resultado.append(produto["nome"])
    return resultado
```

Essa função sozinha resolve o Desafio 3 do README para **qualquer**
combinação de tipo e preço máximo que você quiser testar — é a integração
de tudo que você aprendeu: `def`, parâmetros, `for`, `if`, `and`, dicionários e `return`.

---

## 7. Resumo do que você precisa saber para os exercícios

- Definir uma função com `def nome(parametros):`
- Diferenciar `return` (devolve valor) de `print` (só mostra na tela)
- Usar múltiplos parâmetros para tornar a função reutilizável
- Escrever funções que recebem e devolvem listas
- Escrever funções que recebem dicionários
- Escrever funções que recebem listas de dicionários e filtram por múltiplos critérios

Agora vá para `exercicios/01_funcoes_basicas.py` e comece a praticar.
