-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT sh.name AS genre, COUNT(tv.genre_id) AS number_of_shows
FROM tv_genres sh RIGHT JOIN tv_show_genres tv
ON
    sh.id = tv.genre_id
GROUP BY sh.name
ORDER BY number_of_shows DESC;