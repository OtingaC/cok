<<<<<<< HEAD
--Retrieve from payments table
SELECT checkNumber, paymentDate, amount FROM payments;
--Retrieve orders that are 'In Process'. descending-orderDate
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;
--'Sales Rep' as job title descending-employeeNumber
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'SalesRep'
ORDER BY employeeNumber DESC;
--Retrieve all columns and records from office table
SELECT *
FROM offices;
--Fetch productName and quantityinStock from products table ascending orde-buyPrice, limit output to 5records
SELECT productName, quantityinStock
FROM products
ORDER BY buyPrice
=======
--Retrieve from payments table
SELECT checkNumber, paymentDate, amount FROM payments;
--Retrieve orders that are 'In Process'. descending-orderDate
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;
--'Sales Rep' as job title descending-employeeNumber
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'SalesRep'
ORDER BY employeeNumber DESC;
--Retrieve all columns and records from office table
SELECT *
FROM offices;
--Fetch productName and quantityinStock from products table ascending orde-buyPrice, limit output to 5records
SELECT productName, quantityinStock
FROM products
ORDER BY buyPrice
>>>>>>> 5722852 (Week2 Database Assignment)
LIMIT 5;