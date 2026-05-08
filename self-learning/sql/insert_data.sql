-- Insert Sample E-commerce Data
INSERT INTO Customers (CustomerID, FirstName, LastName, Email, RegistrationDate) VALUES
(1, 'Alice', 'Smith', 'alice@example.com', '2023-01-15'),
(2, 'Bob', 'Jones', 'bob@example.com', '2023-02-20'),
(3, 'Charlie', 'Brown', 'charlie@example.com', '2023-03-10');

INSERT INTO Products (ProductID, ProductName, Category, Price, StockQuantity) VALUES
(101, 'Laptop', 'Electronics', 999.99, 50),
(102, 'Smartphone', 'Electronics', 699.50, 150),
(103, 'Desk Chair', 'Furniture', 120.00, 200);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount, Status) VALUES
(1001, 1, '2023-04-01 10:30:00', 999.99, 'Shipped'),
(1002, 2, '2023-04-02 14:15:00', 819.50, 'Processing');
