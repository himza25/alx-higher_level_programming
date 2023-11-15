-- Script to list records with names from second_table ordered by score

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
