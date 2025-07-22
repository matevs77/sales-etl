# load.py
from sqlalchemy import create_engine
import pandas as pd

def load_data(df, db_url, table_name='vendas'):
    if df is None:
        print("Nenhum dado para carregar.")
        return
    
    try:
        # Criar conexão com o SQL Server
        engine = create_engine(db_url)
        
        # Carregar os dados na tabela
        df.to_sql(table_name, engine, if_exists='replace', index=False, schema='dbo')
        print(f"Dados carregados com sucesso na tabela {table_name}.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")