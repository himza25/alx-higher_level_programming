-- List all genres by their rating from hbtn_0d_tvshows_rate
SELECT tv_genres.name, SUM(tv_shows_rate.rating) AS rating
FROM tv_shows_rate
JOIN tv_shows ON tv_shows.id = tv_shows_rate.show_id
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
