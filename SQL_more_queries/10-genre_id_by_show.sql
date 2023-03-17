-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT ts.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON 
	ts.id = tv_show_genres.ts_id
ORDER BY ts.title ASC, tv_show_genres.genre_id ASC;