-- This script lists all TV shows from the database with their ratings
-- It calculates the sum of ratings for each show and displays them
-- Results are sorted in descending order by the rating sum
-- It uses LEFT JOIN to include all shows, even if they don't have ratings
-- It groups results by show title and orders them by the rating sum in descending order
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
