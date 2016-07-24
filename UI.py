from Movies import MovieLibrary
from Ratings import RatingLibrary


x = int(input("""\t Welcome to your personal movie advisor. \n
\tPlease enter:\n 1 for a print out of all the movies and their id,
 2 to search for a movie by its id,\n 3 to search for the ratings for a specific movie,
 4 the average rating of a movie,\n 5 for ratings by a single user:  """))


while x not in [1, 2, 3, 4, 5]:
    x = int(input("Please enter 1, 2, 3, 4, or 5: "))
    if x == 1:
        MovieLibrary.print_out_movies
    elif x == 2:
        MovieLibrary.find_movie_by_ID
    elif x == 3:
        RatingLibrary.find_rating_by_ID
    elif x == 4:
        RatingLibrary.average_rating_by_ID
    elif x == 5:
        RatingLibrary.ratings_from_single_user
    else:
        print("Please enter a valid number")
