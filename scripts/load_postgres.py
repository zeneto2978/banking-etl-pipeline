# Importa bibliotecas necessárias
import pandas as pd
from sqlalchemy import create_engine, text

# --------------------------------------------------
# CONFIGURAÇÃO DA CONEXÃO COM O POSTGRESQL
# --------------------------------------------------
# Ajuste usuário, senha, host, porta e nome do banco
DB_URI = "postgresql://postgres:postgres@localhost:5433/banking_db"

# Cria o objeto de conexão
engine = create_engine(DB_URI)

# --------------------------------------------------
# LEITURA DOS ARQUIVOS DA CAMADA SILVER
# --------------------------------------------------
clients = pd.read_csv("data/silver/clients.csv")
accounts = pd.read_csv("data/silver/accounts.csv")
transactions = pd.read_csv("data/silver/transactions.csv")

# --------------------------------------------------
# LIMPEZA DAS TABELAS ANTES DA CARGA
# --------------------------------------------------
# Isso evita duplicação caso você rode o script mais de uma vez
with engine.begin() as conn:
    conn.execute(
        text("TRUNCATE TABLE transactions, accounts, clients RESTART IDENTITY CASCADE")
    )

# --------------------------------------------------
# CARGA DOS DADOS PARA O POSTGRESQL
# --------------------------------------------------
clients.to_sql("clients", engine, if_exists="append", index=False)
accounts.to_sql("accounts", engine, if_exists="append", index=False)
transactions.to_sql("transactions", engine, if_exists="append", index=False)

# Mensagem final
print("Dados carregados no PostgreSQL com sucesso.")