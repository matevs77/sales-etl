# main.py
from extract import extract_data
from transform import transform_data
from load import load_data
from config import API_URL, DB_URL

def run_etl():
    raw_data = extract_data(API_URL)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data, DB_URL)

if __name__ == "__main__":
    run_etl()