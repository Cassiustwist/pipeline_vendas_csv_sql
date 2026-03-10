import pandas as pd
from pathlib import Path

# Caminhos dos arquivos
RAW_PATH = Path("data/raw/sales_raw.csv")
BRONZE_PATH = Path("data/bronze/sales_bronze.csv")


def main():

    # 1. Ler CSV RAW
    df = pd.read_csv(RAW_PATH)

    # 2. Padronizar nomes das colunas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 3. Remover espaços extras nos textos
    df["customer_name"] = df["customer_name"].str.strip()
    df["product"] = df["product"].str.strip()
    df["category"] = df["category"].str.strip()
    df["city"] = df["city"].str.strip()

    # 4. Padronizar textos
    df["category"] = df["category"].str.lower()
    df["city"] = df["city"].str.title()

    # 5. Converter tipos numéricos
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].astype(float)

    # 6. Criar coluna de valor total
    df["total_value"] = df["quantity"] * df["unit_price"]

    # 7. Salvar CSV BRONZE
    df.to_csv(BRONZE_PATH, index=False)

    print("Arquivo bronze gerado com sucesso!")


if __name__ == "__main__":
    main()