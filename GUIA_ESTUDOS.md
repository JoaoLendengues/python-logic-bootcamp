# 📖 Guia de Estudos - Python Logic Bootcamp

## 🎯 Objetivo Deste Guia

Você vai aprender a aprender programação. Este guia explica **como** você deve estudar cada semana.

---

## 📋 Antes de Começar

### Checklist Inicial

- [ ] Python 3.8+ instalado (`python --version`)
- [ ] VS Code ou editor instalado
- [ ] Git configurado (`git config --list`)
- [ ] Repositório clonado no seu computador
- [ ] Ambiente virtual criado (`python -m venv venv`)

---

## 🔄 Rotina Semanal Recomendada

### Segunda a Quinta (4 dias)

```
SEGUNDA
├─ 09:00 - Ler AULA.md da semana (15 min)
├─ 09:15 - Fazer Exercício 01 (30 min)
├─ 09:45 - Ver solução comentada (10 min)
├─ 09:55 - Fazer commit (5 min)
└─ Total: ~60 minutos

TERÇA
├─ 09:00 - Fazer Exercício 02 (30 min)
├─ 09:30 - Ver solução (10 min)
├─ 09:40 - Fazer commit (5 min)
└─ Total: ~45 minutos

QUARTA
├─ 09:00 - Fazer Exercício 03 (30 min)
├─ 09:30 - Ver solução (10 min)
├─ 09:40 - Fazer commit (5 min)
└─ Total: ~45 minutos

QUINTA
├─ 09:00 - Fazer Exercício 04 (30 min)
├─ 09:30 - Ver solução (10 min)
├─ 09:40 - Fazer commit (5 min)
└─ Total: ~45 minutos
```

### Sexta (Revisão)

```
SEXTA
├─ 09:00 - Revisar toda a semana (20 min)
├─ 09:20 - Fazer DESAFIO SEMANA (45 min)
├─ 10:05 - Ver solução (10 min)
├─ 10:15 - Fazer commit (5 min)
└─ Total: ~90 minutos

Criar um arquivo REFLEXAO.md escrevendo:
- O que aprendeu
- O que foi difícil
- O que foi fácil
- Próximos passos
```

### Sábado e Domingo

```
[ ] Descanso total ou
[ ] Praticar exercícios extras
[ ] Refazer exercícios sem olhar solução
[ ] Criar variações dos exercícios
```

---

## 🚀 Passo a Passo: Como Fazer Um Exercício

### Exemplo: Exercício 01 da Semana 1

#### **PASSO 1: Abra o arquivo (5 min)**

```bash
# Terminal
cd python-logic-bootcamp
code semana_1/exercicios/01_condicional_basico.py
```

Você verá algo como:

```python
"""
EXERCÍCIO 1.1 - Verificar Maior de Idade

PROBLEMA:
Criar um programa que verifica se uma pessoa pode dirigir.
- Se idade >= 18: imprimir "Pode dirigir"
- Se idade < 18: imprimir "Não pode dirigir"

EXEMPLO:
Entrada: idade = 25
Saída esperada: "Pode dirigir"

DICAS:
1. Use if/else
2. Compare a idade com 18
3. Use print() para mostrar resultado
"""

# ESCREVA SEU CÓDIGO AQUI
idade = 25

# ↓ COMPLETE ABAIXO ↓
```

#### **PASSO 2: Tente resolver (25 min)**

**IMPORTANTE:** Sem copiar solução!

```python
# Sua tentativa poderia ser:
idade = 25

if idade >= 18:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
```

#### **PASSO 3: Teste seu código (5 min)**

```bash
# Terminal
python semana_1/exercicios/01_condicional_basico.py
```

**Esperado:** 
```
Pode dirigir
```

#### **PASSO 4: Se funcionou, ir para PASSO 6**

#### **PASSO 5: Se deu erro, o que fazer?**

**Cenário A: SyntaxError**
```
SyntaxError: expected ':'
```
Significa: Você esqueceu `:` depois do `if`

**Cenário B: Logic Error**
```
Seu output: "Não pode dirigir"
Esperado: "Pode dirigir"
```
Significa: Sua lógica está errada. Revise o if/else.

**O que fazer:**
1. Releia o código com calma
2. Procure por erros de digitação
3. Revise a dica no arquivo
4. Se não conseguir, olhe APENAS a dica em SOLUÇÕES.md
5. Tente novamente

#### **PASSO 6: Revise a solução (10 min)**

Abra `SOLUÇÕES.md` e leia:

```python
# SOLUÇÃO ESPERADA:
idade = 25

if idade >= 18:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

# POR QUÊ FUNCIONA:
# - if verifica: "idade >= 18"?
# - Se SIM: executa o bloco if (print "Pode dirigir")
# - Se NÃO: executa o bloco else (print "Não pode dirigir")
# - Com idade = 25, a condição é TRUE, então "Pode dirigir"
```

**LEIA COM ATENÇÃO.** Procure entender cada parte.

#### **PASSO 7: Refaça o exercício (5 min)**

Agora que viu a solução, **feche o arquivo de soluções** e refaça o exercício.

Seu código deve sair naturalmente, sem colar.

#### **PASSO 8: Teste variações (10 min - OPCIONAL)**

Seu código funciona para 25. E para outros números?

```python
# Teste com valores diferentes
idade = 15  # Esperado: "Não pode dirigir"
idade = 18  # Esperado: "Pode dirigir"
idade = 0   # Esperado: "Não pode dirigir"
```

#### **PASSO 9: Faça commit (5 min)**

```bash
# No terminal
git add semana_1/exercicios/01_condicional_basico.py
git commit -m "feat: semana 1 - exercício 01 completo"
git push
```

---

## 🎓 Estrutura de Um Arquivo de Exercício

Todo arquivo segue este padrão:

```python
"""
EXERCÍCIO X.Y - Título

PROBLEMA:
[Descrição clara do que você precisa fazer]

EXEMPLO:
Entrada: [dados de entrada]
Saída esperada: [resultado esperado]

DICAS:
1. [dica 1]
2. [dica 2]
3. [dica 3]
"""

# ESCREVA SEU CÓDIGO AQUI
```

---

## 📝 Atualizando Seu Progresso

A cada exercício completo, atualize `PROGRESSO.md`:

```markdown
# Progresso - Semana 1

Data de Início: 08/07/2026

## Exercícios Completos

- [x] SEG 08/07 - Exercício 01 ✓
- [x] TER 09/07 - Exercício 02 ✓
- [ ] QUA 10/07 - Exercício 03
- [ ] QUI 11/07 - Exercício 04
- [ ] SEX 12/07 - Desafio Semana

## Reflexões da Semana

- Fácil: If/else é mais simples do que parecia
- Difícil: Entender quando usar > vs >=
- Aprendi: Como testar com diferentes valores
```

---

## 🛠️ Troubleshooting

### Problema: "ModuleNotFoundError"

```bash
# Solução:
# Certifique que seu ambiente virtual está ativado

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Problema: "Arquivo não encontrado"

```bash
# Solução:
# Você está na pasta correta?
pwd  # ou cd no Windows

# Deve estar em:
# /seu/caminho/python-logic-bootcamp
```

### Problema: "Não consigo entender o exercício"

```
1. Releia o PROBLEMA com calma
2. Veja o EXEMPLO (entrada/saída)
3. Leia as DICAS
4. Se ainda não entender, abra SOLUÇÕES.md
5. NÃO COPIE, apenas leia
6. Tente fazer sem olhar
7. Se não conseguir, deixa pra outro dia
```

---

## 🎬 Regras de Ouro

### ✅ FAÇA ISSO

- ✅ Tente resolver sozinho SEMPRE
- ✅ Pratique todos os dias
- ✅ Revise as soluções com atenção
- ✅ Faça commits regulares
- ✅ Refaça exercícios sem olhar solução
- ✅ Crie variações dos exercícios
- ✅ Ensine alguém do que aprendeu

### ❌ NÃO FAÇA ISSO

- ❌ Copiar solução diretamente
- ❌ Pular exercícios
- ❌ Programar apenas 1x por semana
- ❌ Passar pra próxima semana sem entender
- ❌ Olhar solução ANTES de tentar
- ❌ Desistir rápido quando travar

---

## 📚 Recursos Extras

Se quiser aprofundar:

- **Python Tutor:** https://pythontutor.com/ (visualizar código executando)
- **Real Python:** https://realpython.com/ (artigos em inglês)
- **W3Schools Python:** https://www.w3schools.com/python/ (referência rápida)

---

## 🎯 Mindset Certo

### Lembre-se:

```
Semana 1: Você vai achar difícil
Semana 2: Vai melhorar
Semana 3: Vai ficar claro
Semana 4: Você vai dominar
```

Cada dia que você pratica, seu cérebro está **criando novas conexões neurais**.

Programação é como **academia:** você não fica forte em 1 dia. Mas em 4 semanas de treino consistente, a mudança é visível.

---

**Você consegue isso! Vamos lá?** 🚀

---

_Criado em: 08/07/2026_
