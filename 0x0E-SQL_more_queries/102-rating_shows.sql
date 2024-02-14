-- This script lists all TV shows from the database with their ratings
-- It calculates the sum of ratings for each show and displays them
-- Results are sorted in descending order by the rating sum
-- It uses LEFT JOIN to include all shows, even if they don't have ratings
-- It groups results by show title and orders them by the rating sum in descending order
SELECT tv_shows.title, SUM(rating) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
