import pandas as pd
from contrato import Compras
from dotenv import load_dotenv
import os

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

        return True, errors

    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, f"Erro inesperado: {str(e)}"