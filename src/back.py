import pandas as pd
from contrato import Compras
from dotenv import load_dotenv
import os

# Variáveis de ambiente
load_dotenv(".env")
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST=os.getenv('POSTGRES_HOST')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')
POSTGRES_DB=os.getenv('POSTGRES_DB')

# Cria string de conexão para parametro do pandas
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def processa_excel(arquivo_carregado):
    try:
        df = pd.read_excel(arquivo_carregado)
        errors = []
        # Verificar se há mais colunas do que deveria
        extra_cols = set(df.columns) - set(Compras.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}"

        # Validar cada linha com o schema do contrato
        for index, row in df.iterrows():
            try:
                _ = Compras(**row.to_dict())
            except Exception as e:
                message = f"Erro na linha {index + 2}: {e}"
                errors.append(message)
                # raise ValueError(message)

        return df,True, errors

    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Erro inesperado: {str(e)}"
    
def excel_to_sql(df):
    df.to_sql('compras', con=DATABASE_URL, if_exists='replace', index=False)