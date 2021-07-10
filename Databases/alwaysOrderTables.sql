CREATE PROCEDURE volleyballResults()
BEGIN
	SELECT *
    FROM results
    ORDER BY wins ASC;
END

CREATE PROCEDURE mostExpensive()
BEGIN
	SELECT MIN(name) as name
    FROM Products
    WHERE price * quantity = (SELECT MAX(price * quantity) from Products);
END