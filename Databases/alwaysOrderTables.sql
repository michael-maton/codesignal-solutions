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

CREATE PROCEDURE gradeDistribution()
BEGIN
	SELECT Name, ID
    FROM Grades
    WHERE Final > ((0.5 * Midterm1) + (0.5 * Midterm2))
    AND Final > ((0.25 * Midterm1) + (0.25 * Midterm2) + (0.5 * Final))
    ORDER BY LEFT(NAME, 3), ID ASC;
END

CREATE PROCEDURE mischievousNephews()
BEGIN
	SELECT WEEKDAY(mischief_date) as "weekday", mischief_date, author, title
    FROM mischief
    ORDER BY weekday ASC,  CASE author 
                           WHEN 'Huey'  THEN 1 
                           WHEN 'Dewey' THEN 2
                           ELSE 3 END, mischief_date, title ASC;
END

CREATE PROCEDURE mischievousNephews()
BEGIN
    SELECT WEEKDAY(mischief_date) as weekday, mischief_date, author, title
    FROM mischief
    ORDER BY 
        weekday,
        length(author),
        author,
        mischief_date,
        title;
END

CREATE PROCEDURE mischievousNephews()
BEGIN
    SELECT WEEKDAY(mischief_date) AS weekday, mischief.*
    FROM mischief
    ORDER BY
        weekday,
        FIELD(author, "Huey", "Dewey", "Louie"),
        mischief_date,
        title ASC;
END