
  create view "banking_db"."public"."stg_accounts__dbt_tmp"
    
    
  as (
    -- Este model prepara a tabela de contas

select
    account_id,         -- ID da conta
    client_id,          -- Cliente relacionado
    account_type,       -- Tipo da conta
    opened_date,        -- Data de abertura
    balance             -- Saldo atual
from accounts
  );