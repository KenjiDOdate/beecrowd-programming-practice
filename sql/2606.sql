SELECT p.id, p.name
FROM products p
JOIN categories c ON P.id_categories = c.id
WHERE c.name LIKE 'super%';