-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT sh.title
FROM tv_shows sh JOIN tv_show_genres tv
ON 
    sh.id = tv.show_id JOIN tv_genres ge ON ge.id = tv.genre_id
WHERE ge.name = 'Comedy'
ORDER BY sh.title;