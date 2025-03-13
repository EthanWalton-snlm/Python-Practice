# SQL Bolt exercises

## Exercise 1

1. Find the title of each film
   ```sql
    SELECT title FROM movies;
   ```
2. Find the director of each film
   ```sql
    SELECT director FROM movies;
   ```
3. Find the title and director of each film
   ```sql
    SELECT title, director FROM movies;
   ```
4. Find the title and year of each film
   ```sql
    SELECT title, year FROM movies;
   ```
5. Find all the information about each film

   ```sql
    SELECT * FROM movies;
   ```

   ![alt text](image.png)

## Exercise 2

1. Find the movie with a row id of 6

   ```sql
    SELECT * FROM movies WHERE Id = 6;
   ```

2. Find the movies released in the years between 2000 and 2010

   ```sql
    SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
   ```

3. Find the movies not released in the years between 2000 and 2010

   ```sql
    SELECT * FROM movies WHERE year NOT BETWEEN 2000 AND 2010;
   ```

4. Find the first 5 Pixar movies and their release year

   ```sql
    SELECT Title, Year FROM movies LIMIT 5;
   ```

   ![alt text](image-1.png)

## Exercise 3

1. Find all the Toy Story movies

   ```sql
    SELECT * FROM movies WHERE Title LIKE 'Toy Story%';
   ```

2. Find all the movies directed by John Lasseter

   ```sql
    SELECT * FROM movies WHERE Director = 'John Lasseter';
   ```

3. Find all the movies (and director) not directed by John Lasseter

   ```sql
    SELECT * FROM movies WHERE Director != 'John Lasseter';
   ```

4. Find all the WALL-\* movies

   ```sql
    SELECT * FROM movies WHERE Title LIKE 'WALL-_';
   ```

   ![alt text](image-2.png)

## Exercise 4

1. List all directors of Pixar movies (alphabetically), without duplicates
   ```sql
    SELECT DISTINCT Director FROM movies ORDER BY Director ASC;
   ```
2. List the last four Pixar movies released (ordered from most recent to least)
   ```sql
    SELECT * FROM movies ORDER BY Year DESC LIMIT 4;
   ```
3. List the first five Pixar movies sorted alphabetically
   ```sql
    SELECT * FROM movies ORDER BY Title, Id ASC LIMIT 5;
   ```
4. List the next five Pixar movies sorted alphabetically

   ```sql
    SELECT * FROM movies ORDER BY Title, Id ASC LIMIT 5 OFFSET 5;
   ```

   ![alt text](image-3.png)

## Exercise 5

1. List all the Canadian cities and their populations
   ```sql
    SELECT City FROM north_american_cities WHERE Country = 'Canada';
   ```
2. Order all the cities in the United States by their latitude from north to south
   ```sql
    SELECT City FROM north_american_cities WHERE Country = 'United States' ORDER BY Latitude DESC;
   ```
3. List all the cities west of Chicago, ordered from west to east
   ```sql
    SELECT City FROM north_american_cities WHERE Longitude < (SELECT Longitude FROM north_american_cities WHERE City = 'Chicago') ORDER BY Longitude ASC;
   ```
4. List the two largest cities in Mexico (by population)
   ```sql
    SELECT City FROM north_american_cities WHERE Country = 'Mexico' ORDER BY Population DESC LIMIT 2;
   ```
5. List the third and fourth largest cities (by population) in the United States and their population
   ```sql
    SELECT City FROM north_american_cities WHERE Country = 'United States' ORDER BY Population DESC LIMIT 2 OFFSET 2;
   ```
   ![alt text](image-4.png)

## Exercise 6
