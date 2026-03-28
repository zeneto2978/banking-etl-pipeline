
  create view "banking_db"."public"."stg_transactions__dbt_tmp"
    
    
  as (
    -- Este model prepara a tabela de transações

select
    transaction_id,     -- ID da transação
    account_id,         -- Conta relacionada
    transaction_date,   -- Data da transação
    transaction_type,   -- Tipo da transação
    amount              -- Valor
from transactions
  );