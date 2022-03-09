-- This script select tvshow titles and genre from the tv show tables and join the show id and the genres id then order them
-- 
FROM tv_shows SELECT tv_shows.titles, tv_shows_genres.genre_id
RIGHT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.titles, tv_shows_genres.genre_id;
