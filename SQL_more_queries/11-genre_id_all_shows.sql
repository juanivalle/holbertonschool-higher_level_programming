-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT sh.title, ge.genre_id
FROM tv_shows sh LEFT JOIN tv_show_genres ge
ON
	sh.id = ge.show_id
ORDER BY sh.title, ge.genre_id;