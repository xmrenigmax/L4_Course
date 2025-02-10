-- Date: 2025/02/10
-- Author: Riley Jordan
-- Description: This script creates a table called city and inserts values into the table. It then selects all from the city table and prints the name of all selected cities.

-- Drop the city table if it exists
DROP TABLE CITY;
-- Creates a table called city
CREATE TABLE CITY
(
    ID NUMBER,
    NAME VARCHAR2(17),
    COUNTRYCODE VARCHAR2(3),
    DISTRICT VARCHAR2(20),
    POPULATION NUMBER
);

-- Merge the city tables data if it exists
    --CITY c stands for the city table "c" is the temporary name for the table
MERGE INTO CITY c
    -- selects values from city table as c and values selected from source table (src)
USING (SELECT 3793 AS ID, 'Kabul' AS NAME, 'AFG' AS COUNTRYCODE, 'Kabol' AS DISTRICT, 1780000 AS POPULATION FROM DUAL) src
    -- ON = join condition, c.ID = src.ID is the condition for the join
ON (c.ID = src.ID)
    -- if condition match, update city table with values from src
WHEN MATCHED THEN
    UPDATE SET c.NAME = src.NAME, c.COUNTRYCODE = src.COUNTRYCODE, c.DISTRICT = src.DISTRICT, c.POPULATION = src.POPULATION
    -- if condition does not match, insert values into city table
WHEN NOT MATCHED THEN
    INSERT (ID,Name,COUNTRYCODE,DISTRICT,POPULATION) 
    VALUES (src.ID, src.NAME, src.COUNTRYCODE, src.DISTRICT, src.POPULATION);

-- select all from the city table
SELECT * FROM CITY;

-- prints the name of all selected cities

SELECT table_name FROM user_tables;

-- new 
SELECT NAME FROM CITY WHERE MOD(2,0) = 0;