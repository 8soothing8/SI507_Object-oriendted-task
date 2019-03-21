
from movies_db import *
# To create the initial database, just import the db object from an interactive Python shell and run the SQLAlchemy.create_all() method to create the tables and database:

import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# Application configurations

app = Flask(__name__)

app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soomovie_list.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy
#
#
# collections = db.Table('collections',db.Column('album_id',db.Integer, db.ForeignKey('albums.id')),db.Column('artist_id',db.Integer, db.ForeignKey('artists.id')))

class Movie_cls(db.Model):
    __tablename__ = 'Movies' # It doesn't need a table name???
    Id = db.Column(db.Integer, primary_key = True)
    Title = db.Column(db.String(250), unique=True)
    Director_Id = db.Column(db.Integer, ForeignKey('Directors.Id'))
    Genre = db.Column(db.String(64))
    Year = db.Column(db.Integer)
    IMDB_rating = db.Column(db.Integer)

#    chocolates = relationship('Chocolate', backref = "Countries_class")

    def __repr__(self):
        return "Title: {} ({})".format(self.Title,self.Year)


class Director_cls(db.Model):
    __tablename__ = 'Directors'
    Id = db.Column(db.Integer, primary_key = True)
    # Title = Column(String(3))
    Name = db.Column(db.String(64))

    def __repr__(self):
        return "{} (ID: {})".format(self.Name,self.Id)

##### Helper functions #####

### For database additions
### Relying on global session variable above existing


def get_or_create_director(director_name):
    director = Director_cls.query.filter_by(Name=director_name).first()
    if director:
        return director
    else:
        director = Director_cls(Name=director_name)
        session.add(director)
        session.commit()
        return director


##### Set up Controllers (route functions) #####

## Main route ##


@app.route('/movie/new/<title>/<director>/<genre>/<year>/<IMDB_rating>/')
def new_movie(title, director, genre, year, IMDB_rating):
    if Movie_cls.query.filter_by(Title=title).first():
        # if there is a title by that title
        return "That movie already exists! Add a new one!"
    else:
        director = get_or_create_director(director)
        movie = Movie_cls(Title=title, Director_Id = director.Id, Genre = genre, Year=year, IMDB_rating = IMDB_rating)
        session.add(movie)
        session.commit()
        return "New movie: {} produced by {} and released in {}. You can see the whole list of movie through .".format(movie.Title, director.Name, movie.Year)

@app.route('/all_movies')
def show_list():
    all_movies = []
    movies = Movie_cls.query.all()

    for m in movies:
        director = Director_cls.query.filter_by(Id=m.Director_Id).first()
        all_movies.append((m.Title, director.Name, m.Genre))

    return "<h1> Hey! Look at my movie list </h1> <br> {}".format(all_movies)

@app.route('/movie/rating/<title>/')
def movie_rate(title):
    if Movie_cls.query.filter_by(Title=title).first():
        search_movie = Movie_cls.query.filter_by(Title=title).first()
        return "The IMDB rating for '{}' is {}".format(search_movie.Title,str(search_movie.IMDB_rating))
    else:
        return "I don't have that movie in my list. Do you want to add it?"


if __name__=='__main__':
	##### CONFIG #####
    db.create_all()
#	movies_list = compose('movies_clean.csv')
    app.run(debug=True)
