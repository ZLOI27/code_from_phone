SELECT customer_name, product_name
FROM customers INNER JOIN orders
ON customers.id = orders.customer_id
ORDER BY customer_name ASC;
