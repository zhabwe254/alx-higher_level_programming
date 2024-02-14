-- This script lists all TV shows without the genre "Comedy"
-- It excludes shows that are associated with the genre "Comedy"
-- Results are sorted in ascending order by the show title
-- It uses LEFT JOIN to include all shows and genres, even if they are not linked
-- It groups results by show title and orders them alphabetically
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name != "Comedy"
GROUP BY tv_shows.title
ORDER BY tv_shows.title ASC;
