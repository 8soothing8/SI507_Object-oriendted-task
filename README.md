# SI507_pjt3

## What it does

This program do the followings for you - 1) adds a new movie by accepting info from users. 2) displays all movies in the list, 3) shows a IMDB rating of a certain movie that a user searches for.

When you run the file 'SI507_project3.py', it will set up two database tables whose names are 'Movies' and 'Directors' individually. Info about a movie that doesn't exist in the database will be recorded in the 'Movies' table and a name of director of the movie will be also populated if the director was not in the 'Directors' table.      

## How to run

First, run the file 'SI507_project3.py' on your prompt.

1) To add a new movie, you need to connect to your local host url and insert information - title, director, genre, released year, and IMDB rating of the movie.

URL: http://localhost:5000/movies/new/<title>/<director>/<genre>/<year>/<IMDB_rating>/

* Fill the < >s with specific information about the movie!

2) To see the entire list of movies stored in the 'Movies' table, link to http://localhost:5000/all_movies.

3) To check a IMDB rating of a certain movie, type the url below and replace the <title> with a title of the movie that you want to look up.

http://localhost:5000/movie/rating/<title>/  
