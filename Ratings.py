import csv
from functools import reduce


class Rating:

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.item_id = kwargs['item_id']
        self.rating = kwargs['rating']
        self.timestamp = kwargs['timestamp']


class RatingLibrary:
        def __init__(self):
            fieldnames = ['user_id', 'item_id', 'rating', 'timestamp']
            self.rows = []
            with open('ml-100k/u.data', 'r') as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter='\t')
                for row in reader:
                    self.rows.append(Rating(**row))

        def find_rating_by_ID(self):
            id_to_find = input("Please enter the ID of the movie you wish to find: ")
            for rating in self.rows:
                if rating.item_id == id_to_find:
                    print(rating.user_id, rating.item_id, rating.rating)

        def average_rating_by_ID(self):
            count = 0
            id_to_find = input("Please enter the ID of the movie you wish to find: ")
            for rating in self.rows:
                count += 1
                if rating.item_id == id_to_find:
                    x = reduce(lambda x, y: x + y, list(map(int, rating.rating)))
                    # return rating.item_id, x
                    print(rating.item_id, x)

        def ratings_from_single_user(self):
            id_to_find = input("Please enter the ID of the movie you wish to find: ")
            for rating in self.rows:
                if rating.user_id == id_to_find:
                    print(rating.user_id, rating.item_id, rating.rating)

        def top_ten_movies(self):
            high_rating = []
            for rating in self.rows:
                if int(rating.rating) >= 4:
                    high_rating.append(rating)
            print(high_rating)
