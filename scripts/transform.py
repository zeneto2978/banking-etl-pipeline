# Importa bibliotecas necessárias
import os
import pandas as pd

# Garante que a pasta silver exista
os.makedirs("data/silver", exist_ok=True)

# --------------------------------------------------
# ETAPA 1: LER OS DADOS DA CAMADA BRONZE
# --------------------------------------------------
# Lemos os arquivos gerados no extract.py
clients = pd.read_csv("data/bronze/clients.csv")
accounts = pd.read_csv("data/bronze/accounts.csv")
transactions = pd.read_csv("data/bronze/transactions.csv")

# --------------------------------------------------
# ETAPA 2: PADRONIZAR NOMES DAS COLUNAS
# --------------------------------------------------
# Deixa todos os nomes de colunas em minúsculo
clients.columns = [col.lower() for col in clients.columns]
accounts.columns = [col.lower() for col in accounts.columns]
transactions.columns = [col.lower() for col in transactions.columns]

# --------------------------------------------------
# ETAPA 3: REMOVER DUPLICADOS
# --------------------------------------------------
# Remove linhas repetidas, caso existam
clients = clients.drop_duplicates()
accounts = accounts.drop_duplicates()
transactions = transactions.drop_duplicates()

# --------------------------------------------------
# ETAPA 4: REMOVER VALORES NULOS
# --------------------------------------------------
# Remove registros com valores ausentes
clients = clients.dropna()
accounts = accounts.dropna()
transactions = transactions.dropna()

# --------------------------------------------------
# ETAPA 5: APLICAR REGRA DE QUALIDADE
# --------------------------------------------------
# Neste exemplo simples, vamos manter apenas valores
# dentro de uma faixa razoável para o cenário didático
transactions = transactions[
    (transactions["amount"] >= -5000) &
    (transactions["amount"] <= 5000)
]

# --------------------------------------------------
# ETAPA 6: SALVAR OS DADOS NA CAMADA SILVER
# --------------------------------------------------
clients.to_csv("data/silver/clients.csv", index=False)
accounts.to_csv("data/silver/accounts.csv", index=False)
transactions.to_csv("data/silver/transactions.csv", index=False)

# Mensagem final
print("Arquivos da camada silver criados com sucesso.")