# Importa bibliotecas necessárias
import os
import random
import pandas as pd
from faker import Faker

# Cria um gerador de dados falsos
fake = Faker()

# Define uma semente fixa para os números aleatórios
# Isso faz o projeto gerar resultados reproduzíveis
random.seed(42)

# Garante que a pasta bronze exista
os.makedirs("data/bronze", exist_ok=True)

# --------------------------------------------------
# ETAPA 1: GERAR CLIENTES
# --------------------------------------------------
# Vamos criar uma lista de clientes fictícios
clients = []

# Loop para criar 100 clientes
for client_id in range(1, 101):
    clients.append({
        "client_id": client_id,         # ID único do cliente
        "full_name": fake.name(),       # Nome falso
        "city": fake.city(),            # Cidade falsa
        "state": fake.state_abbr()      # Sigla do estado
    })

# Converte a lista em DataFrame
df_clients = pd.DataFrame(clients)

# --------------------------------------------------
# ETAPA 2: GERAR CONTAS
# --------------------------------------------------
# Cada conta ficará associada a um cliente
accounts = []

for account_id in range(1, 101):
    accounts.append({
        "account_id": account_id,                              # ID único da conta
        "client_id": account_id,                              # Liga a conta ao cliente
        "account_type": random.choice(["checking", "savings"]),  # Tipo da conta
        "opened_date": fake.date_between(start_date="-3y", end_date="today"),  # Data de abertura
        "balance": round(random.uniform(500, 20000), 2)       # Saldo inicial aleatório
    })

df_accounts = pd.DataFrame(accounts)

# --------------------------------------------------
# ETAPA 3: GERAR TRANSAÇÕES
# --------------------------------------------------
# Agora vamos gerar 1000 transações fictícias
transactions = []

for transaction_id in range(1, 1001):
    transactions.append({
        "transaction_id": transaction_id,  # ID da transação
        "account_id": random.randint(1, 100),  # Conta aleatória entre 1 e 100
        "transaction_date": fake.date_between(start_date="-12M", end_date="today"),  # Data
        "transaction_type": random.choice([
            "pix",
            "debit_card",
            "credit_card",
            "transfer",
            "withdrawal",
            "deposit"
        ]),
        "amount": round(random.uniform(-1500, 3000), 2)  # Valor da transação
    })

df_transactions = pd.DataFrame(transactions)

# --------------------------------------------------
# ETAPA 4: SALVAR ARQUIVOS NA CAMADA BRONZE
# --------------------------------------------------
# Salva cada DataFrame como CSV
df_clients.to_csv("data/bronze/clients.csv", index=False)
df_accounts.to_csv("data/bronze/accounts.csv", index=False)
df_transactions.to_csv("data/bronze/transactions.csv", index=False)

# Mensagem final
print("Arquivos da camada bronze criados com sucesso.")