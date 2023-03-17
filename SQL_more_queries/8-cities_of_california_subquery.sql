-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT cities.id, states.id FROM states, cities WHERE states.name = "california" AND cities.states_id = states.id ORDER BY cities.id ASC;