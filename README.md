#  Projeto Aplicado – Análise Exploratória de Dados (PETR4)

##  Descrição do Projeto

Este projeto tem como objetivo realizar uma **Análise Exploratória de Dados (EDA)** sobre o comportamento das ações da empresa Petrobras (PETR4), utilizando dados históricos do mercado financeiro.

A análise busca identificar padrões, tendências e relações entre variáveis como preço de abertura, fechamento, máximas, mínimas e volume de negociação.

---

##  Objetivo

Realizar uma análise exploratória para responder perguntas como:

* Como o preço da ação evoluiu ao longo do tempo?
* Existe padrão entre preço e volume?
* Qual o nível de volatilidade do ativo?
* Há correlação entre os preços (open, close, high, low)?

---

##  Dataset

Os dados foram obtidos de forma dinâmica através da API do Yahoo Finance, utilizando a biblioteca `yfinance`.

 Características:

* Frequência: diária
* Período: 2000 a 2025
* Tipo: dados históricos de mercado financeiro

 Variáveis:

* `date` → Data da negociação
* `open` → Preço de abertura
* `high` → Preço máximo
* `low` → Preço mínimo
* `close` → Preço de fechamento
* `volume` → Volume negociado

---

##  Tecnologias Utilizadas

* Python 
* Pandas
* Matplotlib
* YFinance
* Git & GitHub

---

##  Análises Realizadas

* ✔ Limpeza e tratamento de dados
* ✔ Conversão de tipos (datas e numéricos)
* ✔ Estatísticas descritivas
* ✔ Análise temporal
* ✔ Correlação entre variáveis
* ✔ Geração de gráficos

---

##  Principais Insights

* Existe **alta correlação** entre os preços (open, high, low, close)
* O ativo apresenta **alta volatilidade ao longo do tempo**
* O volume de negociação varia significativamente, indicando períodos de maior atividade do mercado
* Os dados permitem análises mais avançadas, como tendências e previsão

---

##  Estrutura do Projeto

```
projeto-aplicado/
│
├── eda_petr4.py              # Script principal de análise exploratória
├── baixar_dados_petr4.py     # Script para gerar o dataset
├── petr4.csv                 # Dataset gerado
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação
└── .gitignore                # Arquivos ignorados pelo Git
```

---

##  Como Executar o Projeto

### 1️ Clonar o repositório

```bash
git clone https://github.com/Leonardo-Gaspar/Projeto-Aplicado-.git
cd Projeto-Aplicado
```

---

### 2️ Criar ambiente virtual (venv)

```bash
python -m venv venv
```

---

### 3️ Ativar o ambiente virtual

#### Windows (CMD):

```bash
venv\Scripts\activate
```

#### Windows (PowerShell):

```bash
venv\Scripts\Activate.ps1
```

---

### 4️ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 5️ Gerar o dataset

```bash
python baixar_dados_petr4.py
```

---

### 6️ Executar a análise exploratória

```bash
python eda_petr4.py
```

---

##  Observações

* O dataset é gerado automaticamente via API, garantindo dados atualizados
* Não são utilizados dados sensíveis
* O projeto possui finalidade acadêmica

---

##  Autor(es)

* Leonardo Gaspar Saheb

---

##  Referências

* Yahoo Finance (dados de mercado)
* Documentação do Pandas
* Documentação do Matplotlib

---

##  Conclusão

Este projeto demonstra como a análise exploratória de dados pode ser aplicada ao mercado financeiro, permitindo extrair insights relevantes e apoiar a tomada de decisão baseada em dados.

---
