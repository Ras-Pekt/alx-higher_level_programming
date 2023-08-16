# 0x0E. SQL - More queries
This directory contains  SQL scripts that perfrom the following actions:
- [0-privileges.sql](0-privileges.sql) - lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`)
- [1-create_user.sql](1-create_user.sql) - creates the MySQL server user `user_0d_1`
- [2-create_read_user.sql](2-create_read_user.sql) - creates the database hbtn_0d_2 and the user user_0d_2
- [3-force_name.sql](3-force_name.sql) - creates the table force_name on your MySQL server
- [4-never_empty.sql](4-never_empty.sql) - creates the table id_not_null on your MySQL server
- [5-unique_id.sql](5-unique_id.sql) - creates the table unique_id on your MySQL server
- [6-states.sql](6-states.sql) - creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
- [7-cities.sql](7-cities.sql) - creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
- [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql) - lists all the cities of California that can be found in the database hbtn_0d_usa
- [9-cities_by_state_join.sql](9-cities_by_state_join.sql) -  lists all cities contained in the database hbtn_0d_usa
- [10-genre_id_by_show.sql](10-genre_id_by_show.sql) - lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
- [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql) - lists all shows contained in the database hbtn_0d_tvshows
- [12-no_genre.sql](12-no_genre.sql) - lists all shows contained in hbtn_0d_tvshows without a genre linked
- [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql) - lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each