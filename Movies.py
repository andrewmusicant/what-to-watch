import csv


class Movie:
    def __init__(self, **kwargs):
        self.movie_id = kwargs['movie_id']
        self.movie_name = kwargs['movie_name']
        self.date_made = kwargs['date_made']
        self.imdb = kwargs['imdb']
        self.unknown = kwargs['unknown']
        self.action = kwargs['action']
        self.adventure = kwargs['adventure']
        self.animation = kwargs['animation']
        self.childrens = kwargs['childrens']
        self.comedy = kwargs['comedy']
        self.crime = kwargs['crime']
        self.documentary = kwargs['documentary']
        self.drama = kwargs['drama']
        self.fantasy = kwargs['fantasy']
        self.film_noir = kwargs['film_noir']
        self.horror = kwargs['horror']
        self.musical = kwargs['musical']
        self.mystery = kwargs['mystery']
        self.romance = kwargs['romance']
        self.sci_fi = kwargs['sci_fi']
        self.thriller = kwargs['thriller']
        self.war = kwargs['war']
        self.western = kwargs['western']

    def __str__(self):
        return "{}{}{}".format(self.movie_id, self.movie_name, self.date_made)


class MovieLibrary:
    def __init__(self):
        fieldnames = ['movie_id', 'movie_name', 'date_made', 'x', 'imdb', 'unknown', 'action', 'adventure', 'animation', 'childrens', 'comedy', 'crime', 'documentary', 'drama', 'fantasy', 'film_noir', 'horror', 'musical', 'mystery', 'romance', 'sci_fi', 'thriller', 'war', 'western']
        self.rows = []
        with open('ml-100k/u.item', encoding='latin_1') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter='|')
            for row in reader:
                self.rows.append(Movie(**row))

    def find_movie_by_ID(self):
        id_to_find = input("Please enter the ID of the movie you wish to find: ")
        for movie in self.rows:
            if movie.movie_id == id_to_find:
                return movie.movie_id, movie.movie_name

    def print_out_movies(self):
        for movie in self.rows:
            return movie.movie_id, movie.movie_name
