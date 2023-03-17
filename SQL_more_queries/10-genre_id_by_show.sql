-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT show.title, show_ge.genre_id
FROM tv_shows show INNER JOIN tv_show_genres show_ge
ON
	show.id = show_ge.show_id
ORDER BY show.title, show_ge.genre_id;