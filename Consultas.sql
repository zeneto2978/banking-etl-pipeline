-- Total transacionado por cliente
SELECT
    c.client_id,
    c.full_name,
    ROUND(SUM(t.amount), 2) AS total_transacionado
FROM clients c
JOIN accounts a
    ON c.client_id = a.client_id
JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY c.client_id, c.full_name
ORDER BY total_transacionado DESC;

-- Quantidade de transações por conta
SELECT
    a.account_id,
    COUNT(t.transaction_id) AS total_transacoes
FROM accounts a
JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY a.account_id
ORDER BY total_transacoes DESC;

-- Média por tipo de transação
SELECT
    transaction_type,
    ROUND(AVG(amount), 2) AS media_valor
FROM transactions
GROUP BY transaction_type
ORDER BY media_valor DESC;

-- Transações potencialmente suspeitas
SELECT
    transaction_id,
    account_id,
    transaction_date,
    transaction_type,
    amount
FROM transactions
WHERE amount > 2000
ORDER BY amount DESC;