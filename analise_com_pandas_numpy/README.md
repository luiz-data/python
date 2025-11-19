# 📊 Análise de Risco e Estoque de Emergência - Pandas & NumPy

## 🎯 Objetivo do Projeto

Este projeto demonstra o uso completo das bibliotecas **Pandas** e **NumPy** através de um problema de negócio real: **priorização de medicamentos e recursos em estoque hospitalar** baseado em análise de alergias de pacientes.

---

## 📁 Estrutura do Dataset

**Arquivo:** `allergies.csv`

**Colunas principais:**
- `PATIENT` - Identificador único do paciente
- `START` - Data de registro da alergia
- `DESCRIPTION` - Descrição da alergia
- `CATEGORY` - Categoria (medication, food, environment)
- `TYPE` - Tipo (allergy, intolerance)
- `SEVERITY1`, `SEVERITY2` - Níveis de severidade (SEVERE, MODERATE, MILD)
- `CODE` - Código de classificação

---

## 🧩 Estrutura do Código

### **1. Importação e Carregamento**
```python
import pandas as pd
import numpy as np
df = pd.read_csv('allergies.csv')
```

**Conceitos:**
- Importação de bibliotecas
- Leitura de CSV com Pandas
- Exploração inicial com `.shape` e `.head()`

**Importância:** Base para qualquer análise de dados, validando que os dados foram carregados corretamente.

---

### **2. NumPy Arrays e Indexação**
```python
severity_array = df['SEVERITY1'].dropna().values
severity_array[:5]   # Primeiros 5
severity_array[-5:]  # Últimos 5
severity_array[10:15] # Slice
```

**Conceitos:**
- Conversão de Series para Array NumPy
- Slicing básico (início, fim, intervalo)
- Indexação negativa

**Importância:** Arrays NumPy são a base para operações vetorizadas de alta performance.

---

### **3. Máscaras Booleanas**
```python
mask_severe = severity_array == 'SEVERE'
mask_critical = mask_severe | mask_moderate
```

**Conceitos:**
- Operações de comparação elemento a elemento
- Operadores lógicos (`|`, `&`, `~`)
- Contagem com `.sum()`

**Importância:** Filtros eficientes sem loops, essenciais para análise de grandes volumes.

---

### **4. Fancy Indexing**
```python
indices = np.array([0, 10, 20, 30, 40])
severity_array[indices]
```

**Conceitos:**
- Indexação com arrays de índices
- Seleção não-contígua

**Importância:** Permite seleção complexa de elementos específicos em uma única operação.

---

### **5. Ufuncs - Operações Vetorizadas**
```python
risk_scores = patient_counts + (severe_counts * 10)
np.mean(risk_scores)
np.median(risk_scores)
np.std(risk_scores)
```

**Conceitos:**
- Universal Functions (ufuncs)
- Operações aritméticas vetorizadas
- Agregações estatísticas

**Importância:** Operações 10-100x mais rápidas que loops Python, essenciais para Big Data.

---

### **6. Agregações NumPy**
```python
unique_cats, counts = np.unique(categories, return_counts=True)
```

**Conceitos:**
- `np.unique()` com contagem
- Valores únicos em arrays

**Importância:** Análise de frequência rápida e eficiente.

---

### **7. Álgebra Linear - Scores Ponderados**
```python
features = np.array([[45, 5, 3], [32, 2, 2]])
weights = np.array([1, 10, 2])
weighted_scores = np.dot(features, weights)
```

**Conceitos:**
- Produto escalar (dot product)
- Multiplicação matricial
- Normalização de dados

**Importância:** Base para Machine Learning e cálculos de scores complexos.

---

### **8. Pandas Series**
```python
severity_series = pd.Series(
    ['SEVERE', 'MODERATE', 'MILD'],
    index=['P1', 'P2', 'P3'],
    name='Severidade'
)
```

**Conceitos:**
- Criação de Series
- Índices customizados
- `.value_counts()`

**Importância:** Estrutura de dados 1D com índices, ideal para séries temporais e categóricas.

---

### **9. DataFrame - Tipos e Info**
```python
df.dtypes
df.shape
df.columns
```

**Conceitos:**
- Exploração de tipos de dados
- Dimensões do DataFrame
- Metadados

**Importância:** Entender a estrutura dos dados antes de qualquer análise.

---

### **10. Conversão de Tipos**
```python
df['START'] = pd.to_datetime(df['START'], errors='coerce')
df['TYPE'].unique()
df['CATEGORY'].unique()
```

**Conceitos:**
- Conversão para datetime
- Identificação de valores únicos
- Tratamento de erros com `errors='coerce'`

**Importância:** Tipos corretos são essenciais para operações específicas (temporal, numérica).

---

### **11. Manipulação de Índices**
```python
df_indexed = df.set_index('PATIENT')
df_reset = df_indexed.reset_index()
```

**Conceitos:**
- `set_index()` - definir coluna como índice
- `reset_index()` - voltar ao índice numérico

**Importância:** Índices semânticos facilitam buscas e joins.

---

### **12. Seleção - loc, iloc, at, iat**
```python
df.loc[0:2, ['DESCRIPTION', 'CATEGORY']]  # Por rótulos
df.iloc[0:3, [6, 8, 10]]                  # Por posição
df.at[0, 'DESCRIPTION']                    # Escalar por rótulo
df.iat[0, 6]                               # Escalar por posição
```

**Conceitos:**
- `loc` - seleção por rótulos
- `iloc` - seleção por posição inteira
- `at/iat` - acesso escalar rápido

**Importância:** Diferentes formas de seleção para diferentes necessidades de performance.

---

### **13. Filtros Booleanos**
```python
severe_df = df[df['SEVERITY1'] == 'SEVERE']
severe_meds = df[(df['SEVERITY1'] == 'SEVERE') & 
                  (df['CATEGORY'] == 'medication')]
critical_cats = df[df['CATEGORY'].isin(['medication', 'food'])]
```

**Conceitos:**
- Filtros simples e compostos
- Operadores lógicos `&`, `|`
- Método `.isin()` para múltiplos valores

**Importância:** Core da análise exploratória, filtrando dados relevantes.

---

### **14. SettingWithCopyWarning - Boas Práticas**
```python
# ✅ CORRETO
df_food = df[df['CATEGORY'] == 'food'].copy()
df_food['RISK_LEVEL'] = 'HIGH'

# ✅ CORRETO
df.loc[df['CATEGORY'] == 'food', 'IS_FOOD'] = True
```

**Conceitos:**
- `.copy()` para criar cópias explícitas
- `.loc[]` para atribuições seguras
- Evitar warnings de cadeia

**Importância:** Previne bugs silenciosos e comportamentos inesperados.

---

### **15. GroupBy - Agregações**
```python
df.groupby('CATEGORY').size()
df.groupby('CATEGORY').agg({
    'PATIENT': ['count', 'nunique']
})
df.groupby(['CATEGORY', 'SEVERITY1']).size().unstack()
```

**Conceitos:**
- Agregações por grupos
- Múltiplas agregações com `.agg()`
- Pivotamento com `.unstack()`

**Importância:** Split-Apply-Combine, padrão fundamental para análise de dados.

---

### **16. Pivot Tables**
```python
pd.pivot_table(
    df,
    values='PATIENT',
    index='CATEGORY',
    columns='SEVERITY1',
    aggfunc='count',
    fill_value=0,
    margins=True  # Totais
)
```

**Conceitos:**
- Tabelas dinâmicas
- Agregações cruzadas
- Totais marginais

**Importância:** Visualização multidimensional de dados, similar ao Excel.

---

### **17. Concat - Concatenação**
```python
df_concat = pd.concat([df_med, df_food], 
                      axis=0, 
                      ignore_index=True)
```

**Conceitos:**
- Concatenação vertical (`axis=0`)
- Concatenação horizontal (`axis=1`)
- Reindexação

**Importância:** Combinar múltiplos DataFrames de mesma estrutura.

---

### **18. Merge - Enriquecimento**
```python
category_info = pd.DataFrame({
    'CATEGORY': ['medication', 'food'],
    'PRIORITY': ['ALTA', 'ALTA']
})
df_enriched = df.merge(category_info, on='CATEGORY', how='left')
```

**Conceitos:**
- Joins entre DataFrames (left, right, inner, outer)
- Enriquecimento de dados
- Chaves de junção

**Importância:** Combinar informações de diferentes fontes (similar a SQL JOIN).

---

### **19. Análise Temporal**
```python
df['YEAR'] = df['START'].dt.year
df['MONTH'] = df['START'].dt.month
df['QUARTER'] = df['START'].dt.quarter
df.groupby('YEAR').size()
```

**Conceitos:**
- Accessor `.dt` para datas
- Extração de componentes temporais
- Agregações temporais

**Importância:** Análise de tendências e sazonalidade.

---

### **20. Rolling Windows**
```python
ts_df['Rolling_3M'] = ts_df['Count'].rolling(3, min_periods=1).mean()
ts_df['Cumsum'] = ts_df['Count'].cumsum()
```

**Conceitos:**
- Médias móveis
- Somas cumulativas
- Janelas deslizantes

**Importância:** Suavização de séries temporais e análise de tendências.

---

### **21. Resolução do Problema de Negócio**

#### **9 Perguntas Respondidas:**

1. **Quantas alergias foram registradas?**
   - Total de registros e percentual do dataset

2. **Qual a distribuição de severidade?**
   - SEVERE, MODERATE, MILD com percentuais

3. **Quais categorias são mais críticas?**
   - Ranking com risk scores ponderados

4. **Quais as 10 alergias mais perigosas?**
   - Top 10 baseado em frequência e severidade

5. **Quais medicamentos priorizar no estoque?**
   - Top 10 medicamentos com scores detalhados

6. **Quantos pacientes únicos são afetados?**
   - Pacientes únicos e média de alergias por paciente

7. **Existe tendência temporal?**
   - Análise de crescimento anual com visualização

8. **Quais alergias alimentares são mais comuns?**
   - Top 5 alimentos alérgenos

9. **Qual a taxa de criticidade por categoria?**
   - Percentual de casos SEVERE+MODERATE

**Importância:** Demonstra como todas as técnicas se combinam para resolver um problema real de negócio.

---

## 🎓 Conceitos Demonstrados

### **NumPy**
- ✅ Arrays e operações vetorizadas
- ✅ Slicing e indexação avançada
- ✅ Máscaras booleanas
- ✅ Fancy indexing
- ✅ Ufuncs (universal functions)
- ✅ Agregações (sum, mean, median, std)
- ✅ Álgebra linear (dot product)
- ✅ Unique e return_counts

### **Pandas**
- ✅ Series e DataFrame
- ✅ Tipos de dados e conversões
- ✅ Índices (set_index, reset_index)
- ✅ Seleção (loc, iloc, at, iat)
- ✅ Filtros booleanos e isin()
- ✅ GroupBy e agregações múltiplas
- ✅ Pivot tables com margins
- ✅ Concat (vertical)
- ✅ Merge (enriquecimento)
- ✅ Análise temporal (dt accessor)
- ✅ Rolling windows
- ✅ Apply com funções customizadas

---

## 🚀 Como Executar

### **Requisitos**
```bash
pip install pandas numpy
```

### **Execução**
```bash
jupyter notebook analise_alergias.ipynb
```

Ou executar célula por célula para entender cada conceito progressivamente.

---

## 📈 Resultados Esperados

### **Insights de Negócio:**
- ✅ Identificação de alergias críticas
- ✅ Priorização de medicamentos no estoque
- ✅ Risk scoring baseado em dados
- ✅ Tendências temporais
- ✅ Segmentação por categoria
- ✅ Recomendações acionáveis

### **Métricas Calculadas:**
- Total de alergias registradas
- Distribuição de severidade
- Risk scores ponderados
- Taxa de criticidade
- Crescimento temporal
- Pacientes de alto risco


## 📚 Referências
- [Dataset](https://synthea.mitre.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Python for Data Analysis (Wes McKinney)](https://wesmckinney.com/book/)

**⭐ Se este material foi útil, considere dar uma estrela no repositório!**
