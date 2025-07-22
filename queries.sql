-- queries.sql

-- Total de vendas por região
SELECT regiao, SUM(valor) AS total_vendas
FROM dbo.vendas
GROUP BY regiao
ORDER BY total_vendas DESC;

-- Vendas por mês
SELECT mes_ano, SUM(valor) AS total_vendas
FROM dbo.vendas
GROUP BY mes_ano
ORDER BY mes_ano;

-- Produtos mais vendidos
SELECT TOP 5 produto, COUNT(*) AS qtd_vendas, SUM(valor) AS total_vendas
FROM dbo.vendas
GROUP BY produto
ORDER BY total_vendas DESC;