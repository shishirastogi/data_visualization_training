-- Advanced Joins and Formatting
SELECT 
    o.OrderID,
    c.FirstName + ' ' + c.LastName AS CustomerFullName,
    o.OrderDate,
    o.TotalAmount,
    o.Status
FROM Orders o
INNER JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE o.Status = 'Shipped'
ORDER BY o.OrderDate DESC;
