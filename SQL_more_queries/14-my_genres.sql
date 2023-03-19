-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT sh.name
FROM tv_genres sh JOIN tv_show_genres tv
ON
    sh.id = tv.genre_id JOIN tv_shows ge ON ge.id = tv.show_id
WHERE ge.title = 'Dexter'
ORDER BY sh.name;