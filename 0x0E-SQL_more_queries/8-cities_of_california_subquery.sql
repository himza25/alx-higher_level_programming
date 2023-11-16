-- List all cities of California in hbtn_0d_usa
SELECT c.id, c.name FROM cities c,
     (SELECT id FROM states WHERE name = 'California') s
WHERE c.state_id = s.id
ORDER BY c.id ASC;
