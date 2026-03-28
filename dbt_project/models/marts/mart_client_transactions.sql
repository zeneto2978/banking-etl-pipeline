-- Este model cria uma tabela analítica final
-- Ele resume as transações por cliente

select
    c.client_id,                               -- ID do cliente
    c.full_name,                               -- Nome do cliente
    count(t.transaction_id) as total_transacoes,   -- Quantidade total de transações
    round(sum(t.amount)::numeric, 2) as total_transacionado,  -- Soma dos valores
    round(avg(t.amount)::numeric, 2) as media_transacao       -- Média das transações
from {{ ref('stg_clients') }} c
join {{ ref('stg_accounts') }} a
    on c.client_id = a.client_id
join {{ ref('stg_transactions') }} t
    on a.account_id = t.account_id
group by
    c.client_id,
    c.full_name
order by total_transacionado desc