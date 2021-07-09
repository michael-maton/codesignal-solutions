CREATE PROCEDURE projectList()
BEGIN
	SELECT project_name, team_lead, income 
    FROM Projects 
    ORDER BY internal_id ASC;
END

CREATE PROCEDURE countriesSelection()
BEGIN
	SELECT *
    FROM countries
    WHERE continent = "Africa"
    ORDER BY name;
END

CREATE PROCEDURE monthlyScholarships()
BEGIN
	SELECT id, scholarship / 12
    FROM scholarships;
END

CREATE PROCEDURE projectsTeam()
BEGIN
	SELECT DISTINCT name
    FROM projectLog
    ORDER BY name ASC;
END

CREATE PROCEDURE automaticNotifications()
    SELECT email
    FROM users
    WHERE role NOT IN ("admin", "premium")

    ORDER BY email;

