-- List all shows by their rating from hbtn_0d_tvshows_rate
SELECT tv_shows.title, SUM(rating) AS rating
FROM tv_shows_rate
JOIN tv_shows ON tv_shows.id = tv_shows_rate.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
