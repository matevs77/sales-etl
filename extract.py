# extract.py
import requests
import pandas as pd

def extract_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        return df
    except requests.RequestException as e:
        print(f"Erro ao extrair dados: {e}")
        return None
        #sqlalchemy pyodbc