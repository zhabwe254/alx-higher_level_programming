-- This script lists all genres from the database with their ratings
-- It calculates the sum of ratings for each genre and displays them
-- Results are sorted in descending order by the rating sum
-- It uses LEFT JOIN to include all genres and shows, even if they are not linked
-- It groups results by genre name and orders them by the rating sum in descending order
SELECT tv_genres.name, SUM(rating) AS rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
