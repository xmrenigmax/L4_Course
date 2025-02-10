-- Date: 2025/02/10
-- Author: Riley Jordan

-- Drops the table city if it exists so that we can create a new one
DROP TABLE CITY
-- Creates a table called city
CREATE TABLE CITY
(
    ID NUMBER,
    NAME VARCHAR2(17),
    COUNTRYCODE VARCHAR2(3),
    DISTRICT VARCHAR2(20),
    POPULATION NUMBER
);

-- Inserts values into the city table
INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (3793, 'Kabul', 'AFG', 'Kabol', 1780000);

-- select all from the city table
SELECT * FROM CITY;

-- prints the name of all selected cities
