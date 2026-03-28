
  create view "banking_db"."public"."stg_clients__dbt_tmp"
    
    
  as (
    -- Este model prepara a tabela de clientes
-- A função ref() aponta para uma tabela já existente no banco

select
    client_id,      -- ID do cliente
    full_name,      -- Nome completo
    city,           -- Cidade
    state           -- Estado
from clients
  );