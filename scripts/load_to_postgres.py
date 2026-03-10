import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# carregar variáveis do .env
load_dotenv()

# caminhos
BRONZE_PATH = Path("data/bronze/sales_bronze.csv")

# pegar variáveis do banco
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# string de conexão
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def main():

    # 1. Ler CSV bronze
    df = pd.read_csv(BRONZE_PATH)

    # 2. Criar engine de conexão
    engine = create_engine(DATABASE_URL)

    # 3. Carregar no banco
    df.to_sql(
        "sales",
        engine,
        if_exists="replace",
        index=False
    )

    print("Dados carregados no PostgreSQL com sucesso!")

if __name__ == "__main__":
    main()