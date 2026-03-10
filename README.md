# Pipeline de Ingestão de Vendas (RAW → BRONZE → POSTGRES)

## Contexto

Você é um Analista de Dados Júnior em uma empresa fictícia chamada **Loja Fácil**, um pequeno varejo que possui várias lojas físicas.

Todos os dias o sistema de vendas exporta um arquivo **CSV com as vendas do dia**.

O problema é que esses arquivos chegam com vários problemas:

- espaços extras nas colunas
- letras maiúsculas/minúsculas inconsistentes
- nomes de colunas despadronizados
- dados difíceis de consultar diretamente

A empresa quer começar a organizar os dados para futuras análises e dashboards.

Para isso vamos construir um **pipeline simples de ingestão de dados**.

---

## Objetivo do Projeto

Criar um pipeline que faça:

1. Ler um CSV bruto de vendas (RAW)
2. Padronizar os dados
3. Salvar os dados tratados na camada BRONZE
4. Carregar os dados no banco PostgreSQL
5. Validar os dados com SQL

Fluxo final:

RAW CSV → BRONZE CSV → PostgreSQL → SQL Validation

---

## Estrutura Final do Projeto

Após concluir todos os passos, o projeto terá a seguinte estrutura:

pipeline_vendas_csv_sql

data/
raw/
sales_raw.csv

bronze/
sales_bronze.csv

scripts/
ingest_sales.py
load_to_postgres.py

sql/
validation_queries.sql

requirements.txt

.env.example

README.md

---

## 1. Criar o Repositório

No GitHub crie um novo repositório chamado:

pipeline_vendas_csv_sql

Depois clone o repositório na sua máquina:

git clone https://github.com/SEU_USUARIO/pipeline_vendas_csv_sql.git

Entre na pasta:

cd pipeline_vendas_csv_sql

---

## 2. Criar Estrutura de Pastas

Criar as pastas necessárias:

mkdir data
mkdir data/raw
mkdir data/bronze
mkdir scripts
mkdir sql

---

## 3. Criar o Arquivo RAW

Criar o arquivo:

data/raw/sales_raw.csv

Conteúdo do arquivo:

Sale ID , Date , Customer Name , Product , Category , Quantity , Unit Price , City
1 , 2025-01-02 , Ana Silva , Notebook , Eletronics , 1 , 3500 , Sao Paulo
2 , 2025-01-02 , Bruno Costa , Mouse , eletronics , 2 , 80 , rio de janeiro
3 , 2025-01-03 , Carla Dias , Teclado , Eletronics , 1 , 150 , Belo Horizonte
4 , 2025-01-03 , Daniel Lima , Monitor , Eletronics , 1 , 900 , sao paulo
5 , 2025-01-04 , Fernanda Rocha , Headset , ELETRONICS , 1 , 200 , Rio de Janeiro

Esse arquivo representa **dados brutos recebidos pela empresa**.

---

## 4. Criar Ambiente Virtual

Criar ambiente virtual:

python -m venv venv

Ativar ambiente virtual.

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

---

## 5. Criar Requirements

Criar arquivo:

requirements.txt

Conteúdo:

pandas
sqlalchemy
psycopg2-binary
python-dotenv

Instalar dependências:

pip install -r requirements.txt

---

## 6. Criar Arquivo de Variáveis de Ambiente

Criar arquivo:

.env

Exemplo:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=analytics
DB_USER=postgres
DB_PASSWORD=postgres

Criar também:

.env.example

Sem a senha real:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=analytics
DB_USER=postgres
DB_PASSWORD=your_password

---

## 7. Script de Ingestão (RAW → BRONZE)

Criar arquivo:

scripts/ingest_sales.py

Esse script será responsável por:

- ler o CSV RAW
- limpar os dados
- padronizar colunas
- gerar o CSV BRONZE

Etapas do script:

1. Ler CSV RAW
2. Padronizar nomes das colunas
3. Remover espaços extras
4. Padronizar texto
5. Criar coluna total_value
6. Salvar CSV BRONZE

---

## 8. Script de Carga para Banco

Criar arquivo:

scripts/load_to_postgres.py

Esse script será responsável por:

1. Ler o CSV BRONZE
2. Conectar ao PostgreSQL
3. Criar tabela caso não exista
4. Inserir dados na tabela sales

Tabela final no banco:

sales

---

## 9. Criar Queries de Validação

Criar arquivo:

sql/validation_queries.sql

Exemplo de queries:

Contagem de registros:

SELECT COUNT(*) FROM sales;

Valor total de vendas:

SELECT SUM(total_value) FROM sales;

Vendas por cidade:

SELECT city, SUM(total_value)
FROM sales
GROUP BY city;

---

## 10. Executar Pipeline

Rodar ingestão:

python scripts/ingest_sales.py

Isso irá gerar:

data/bronze/sales_bronze.csv

Depois rodar carga no banco:

python scripts/load_to_postgres.py

---

## 11. Validar Dados no Banco

Abrir PostgreSQL ou ferramenta de consulta SQL.

Executar queries do arquivo:

sql/validation_queries.sql

Verificar:

- número de registros
- soma de vendas
- dados por cidade

---

## Fluxo Final do Pipeline

1. CSV bruto chega na pasta RAW
2. Script limpa e padroniza os dados
3. CSV tratado é salvo na camada BRONZE
4. Script carrega dados no PostgreSQL
5. SQL valida os dados carregados

RAW → BRONZE → DATABASE → SQL VALIDATION

---

## Tecnologias Utilizadas

Python  
Pandas  
PostgreSQL  
SQLAlchemy  
Git  
GitHub

---

## Próximos Passos (Evolução)

Este projeto é apenas o primeiro passo.

Evoluções possíveis:

- adicionar camada SILVER
- adicionar validações automáticas
- orquestrar pipeline
- conectar Power BI
- automatizar ingestões diárias
