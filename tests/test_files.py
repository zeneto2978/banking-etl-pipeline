# Importa bibliotecas necessárias
import os
import pandas as pd

# --------------------------------------------------
# TESTE 1: VERIFICAR SE OS ARQUIVOS BRONZE EXISTEM
# --------------------------------------------------
def test_bronze_files_exist():
    assert os.path.exists("data/bronze/clients.csv")
    assert os.path.exists("data/bronze/accounts.csv")
    assert os.path.exists("data/bronze/transactions.csv")

# --------------------------------------------------
# TESTE 2: VERIFICAR SE OS ARQUIVOS SILVER EXISTEM
# --------------------------------------------------
def test_silver_files_exist():
    assert os.path.exists("data/silver/clients.csv")
    assert os.path.exists("data/silver/accounts.csv")
    assert os.path.exists("data/silver/transactions.csv")

# --------------------------------------------------
# TESTE 3: VERIFICAR SE O ARQUIVO DE CLIENTES NÃO ESTÁ VAZIO
# --------------------------------------------------
def test_clients_file_not_empty():
    df = pd.read_csv("data/silver/clients.csv")
    assert len(df) > 0

# --------------------------------------------------
# TESTE 4: VERIFICAR SE A COLUNA 'amount' EXISTE
# --------------------------------------------------
def test_transactions_file_has_amount_column():
    df = pd.read_csv("data/silver/transactions.csv")
    assert "amount" in df.columns