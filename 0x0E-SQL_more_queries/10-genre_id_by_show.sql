-- This script select tvshow titles and genre from the tv show tables and join the show id and the genres id then order them
-- 
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;