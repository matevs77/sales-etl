# config.py
DB_SERVER = "localhost\\SQLEXPRESS"  # Ou o nome do servidor
DB_NAME = "VendasDB"
DB_USER = "seu_usuario"
DB_PASSWORD = "sua_senha"
DB_URL = f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"
API_URL = "https://api.exemplo.com/vendas"