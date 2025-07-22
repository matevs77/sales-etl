# transform.py
import pandas as pd

def transform_data(df):
    if df is None:
        return None
    
    df = df.drop_duplicates()
    df = df.fillna({'valor': 0, 'regiao': 'Desconhecida'})
    df['data'] = pd.to_datetime(df['data'])
    df['mes_ano'] = df['data'].dt.to_period('M')
    df['regiao'] = df['regiao'].str.upper()
    
    return df