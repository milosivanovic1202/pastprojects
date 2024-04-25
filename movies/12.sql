SELECT title FROM movies, stars, people
WHERE stars.movie_id=movies.id
AND stars.person_id=people.id
AND people.name="Bradley Cooper"
AND title in (
SELECT title FROM movies, stars, people
WHERE stars.movie_id=movies.id
AND stars.person_id=people.id
AND people.name="Jennifer Lawrence"
);