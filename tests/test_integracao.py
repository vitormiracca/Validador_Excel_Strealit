import pandas as pd
import os
from dotenv import load_dotenv

# Variáveis de ambiente
load_dotenv(".env")
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST=os.getenv('POSTGRES_HOST')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')
POSTGRES_DB=os.getenv('POSTGRES_DB')

# Cria string de conexão para parametro do pandas
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def test_read_data_and_check_schema():
    df = pd.read_sql('SELECT * FROM compras', con=DATABASE_URL)

    # Verificar se o DataFrame não está vazio
    assert not df.empty, "O DataFrame está vazio!!!"

    # Verificar o schema (colunas e tipos de dados)
    expected_dtype = {
        'Data': 'datetime64[ns]',
        'Fornecedor': 'object',
        'Categoria': 'object',
        'Produto': 'object',
        'Quantidade':	'int64',
        'Valor_Unitario':	'float64',
        'Email_Fornecedor': 'object',
        'Desconto': 'float64',
        'Valor_Final': 'float64'
    }

    print(df.dtypes.to_dict())
    assert df.dtypes.to_dict() == expected_dtype, "O schema do DataFrame não corresponde ao esperado."