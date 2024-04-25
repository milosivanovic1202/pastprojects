SELECT name FROM people, stars, movies
WHERE stars.person_id = people.id
AND stars.movie_id = movies.id
AND movies.id in
(SELECT movies.id FROM movies
JOIN people ON stars.person_id=people.id
JOIN stars ON stars.movie_id=movies.id
WHERE people.name="Kevin Bacon"
AND people.birth=1958)
AND people.name != "Kevin Bacon";