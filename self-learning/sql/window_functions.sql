-- Window Functions for Analytics
SELECT 
    CustomerID,
    OrderDate,
    TotalAmount,
    SUM(TotalAmount) OVER(PARTITION BY CustomerID ORDER BY OrderDate) AS RunningTotal,
    RANK() OVER(ORDER BY TotalAmount DESC) AS SalesRank,
    LEAD(OrderDate) OVER(PARTITION BY CustomerID ORDER BY OrderDate) AS NextOrderDate
FROM Orders;
