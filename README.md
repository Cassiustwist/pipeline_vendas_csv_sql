# Pipeline de Dados - CSV para PostgreSQL

Este projeto foi criado como parte do meu processo de aprendizado em **engenharia de dados**.

A ideia é simular um pequeno pipeline de dados que:

1. Lê um arquivo CSV com dados de vendas
2. Limpa e organiza os dados usando Python
3. Gera um arquivo tratado (camada Bronze)
4. Carrega os dados em um banco PostgreSQL
5. Realiza consultas SQL para validação

---

# Objetivo do projeto

Praticar conceitos básicos de engenharia de dados:

* ingestão de dados
* transformação de dados
* carga em banco de dados
* validação com SQL
* organização de projetos com Git e GitHub

---

# Fluxo do pipeline

sales_raw.csv
↓
script Python (ingest_sales.py)
↓
arquivo tratado (sales_bronze.csv)
↓
script de carga (load_to_postgres.py)
↓
tabela `sales` no PostgreSQL
↓
consultas de validação em SQL

---

# Estrutura do projeto

```
pipeline_vendas_csv_sql
│
├── data
│   └── raw
│       └── sales_raw.csv
│
├── scripts
│   ├── ingest_sales.py
│   └── load_to_postgres.py
│
├── sql
│   └── validation_queries.sql
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# O que o pipeline faz

O script de ingestão:

* padroniza nomes de colunas
* remove espaços extras
* padroniza textos
* converte tipos numéricos
* cria a coluna `total_value`

Exemplo de cálculo:

```
total_value = quantity * unit_price
```

Depois disso os dados são carregados no PostgreSQL na tabela **sales**.

---

# Consultas de validação

Alguns exemplos de consultas usadas para validar os dados:

```
SELECT COUNT(*) FROM sales;

SELECT SUM(total_value) FROM sales;

SELECT city, SUM(total_value)
FROM sales
GROUP BY city;
```

---

# Como executar o projeto

Clonar o repositório:

```
git clone https://github.com/Cassiustwist/pipeline_vendas_csv_sql.git
```

Criar ambiente virtual:

```
python -m venv venv
```

Ativar o ambiente:

```
venv\Scripts\activate
```

Instalar dependências:

```
pip install -r requirements.txt
```

Executar ingestão:

```
python scripts/ingest_sales.py
```

Carregar no banco:

```
python scripts/load_to_postgres.py
```

---

# Observação

Este é um projeto de estudo para praticar conceitos básicos de engenharia de dados.
