CREATE PROCEDURE volleyballResults()
BEGIN
	SELECT *
    FROM results
    ORDER BY wins ASC;
END

CREATE PROCEDURE mostExpensive()
BEGIN
	SELECT MIN(name) as name /* MIN(name) lexicographically sorts names */
    FROM Products
    WHERE price * quantity = (SELECT MAX(price * quantity) from Products);
END

CREATE PROCEDURE mostExpensive()
BEGIN
	SELECT name 
    FROM Products 
    ORDER BY price * quantity DESC, name ASC LIMIT 1; /* lexicographically sorts names */
END

CREATE PROCEDURE contestLeaderboard()
BEGIN
	SELECT name 
    FROM leaderboard
    ORDER BY score DESC limit 5
    OFFSET 3;
END

CREATE PROCEDURE contestLeaderboard()
BEGIN
	SELECT name FROM leaderboard
     ORDER BY score DESC
     LIMIT 3,5;
END