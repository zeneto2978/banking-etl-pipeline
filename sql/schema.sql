-- Remove as tabelas se já existirem
-- Isso evita erro ao recriar o projeto do zero
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS clients;

-- Cria a tabela de clientes
CREATE TABLE clients (
    client_id INT PRIMARY KEY,         -- ID único do cliente
    full_name VARCHAR(150),            -- Nome completo
    city VARCHAR(100),                 -- Cidade
    state VARCHAR(20)                  -- Estado
);

-- Cria a tabela de contas
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,        -- ID único da conta
    client_id INT,                     -- Cliente dono da conta
    account_type VARCHAR(50),          -- Tipo da conta
    opened_date DATE,                  -- Data de abertura
    balance NUMERIC(12,2),             -- Saldo
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- Cria a tabela de transações
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,    -- ID da transação
    account_id INT,                    -- Conta relacionada
    transaction_date DATE,             -- Data da transação
    transaction_type VARCHAR(50),      -- Tipo da transação
    amount NUMERIC(12,2),              -- Valor da transação
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);