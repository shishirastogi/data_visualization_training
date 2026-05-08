-- Sales Aggregations
SELECT 
    p.Category,
    COUNT(p.ProductID) AS ProductCount,
    AVG(p.Price) AS AveragePrice,
    SUM(p.StockQuantity) AS TotalStock
FROM Products p
GROUP BY p.Category
HAVING COUNT(p.ProductID) > 0
ORDER BY TotalStock DESC;
