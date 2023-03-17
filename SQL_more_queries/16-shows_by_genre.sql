-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT sh.title, ge.name 
FROM tv_shows sh LEFT JOIN tv_show_genres tv
ON
    sh.id = tv.show_id LEFT JOIN tv_genres ge ON ge.id = tv.genre_id
ORDER BY sh.title, ge.name;