import csv
import operator


class Rating:
    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.movie_id = kwargs['movie_id']
        self.rating = float(kwargs['rating'])
        self.timestamp = kwargs['timestamp']


class RatingLibrary:
        def __init__(self):
            fieldnames = ['user_id', 'movie_id', 'rating', 'timestamp']
            self.ratings = []
            self.ratings_by_movie_id = {}
            self.ratings_by_user_id = {}
            with open('ml-100k/u.data', 'r') as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter='\t')
                for row in reader:
                    rating = Rating(**row)
                    self.ratings.append(rating)
                    self.ratings_by_movie_id.setdefault(rating.movie_id, []).append(rating)
                    self.ratings_by_user_id.setdefault(rating.user_id, []).append(rating)

        def find_ratings_by_movie_id(self):
            id_to_find = input("Please enter the ID of the movie you wish to find: ")
            return self.ratings_by_movie_id[id_to_find]

        def average_rating_by_movie_id(self, ratings):
            ratings = [r.rating for r in ratings]
            return sum(ratings) / len(ratings)

        def ratings_from_single_user(self):
            id_to_find = input("Please enter the ID of the user you wish to find: ")
            if id_to_find not in self.ratings_by_user_id:
                return 0
            ratings = self.ratings_by_user_id[id_to_find]
            for rating in ratings:
                print(rating.user_id, rating.movie_id, rating.rating)

        def top_ten_movies(self, minimum_ratings=10):
            movie_ratings = []

            for movie_id in self.ratings_by_movie_id:
                ratings = self.ratings_by_movie_id[movie_id]
                if len(ratings) >= minimum_ratings:
                    average_rating = self.average_rating_by_movie_id(ratings)
                    movie_ratings.append((movie_id, average_rating))

            movie_ratings = sorted(movie_ratings, key=operator.itemgetter(1), reverse=True)

            return movie_ratings[:10]
