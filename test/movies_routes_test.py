import unittest
from routes.movies_routes import get_movie_by_name, get_all_movies, delete_movie_by_name, add_movie, update_movie
from models.Movie import Movie


class EndPointsTest(unittest.TestCase):
    def test_get_movie_by_name(self):
        name_movie = "Star Wars The Return of the Jedi"
        movie = get_movie_by_name(name_movie)
        self.assertEqual(name_movie, movie["name"])

    def test_get_all_movies(self):
        movies: list[Movie] = get_all_movies()
        self.assertEqual(2, len(movies))

    def test_add_movie(self):
        movie = Movie(name="Avatar",
                      actors="Sam Worthington, Zoe Saldaña, Sigourney Weaver, Stephen Lang, Michelle Rodríguez",
                      director="James Cameron",
                      genre="Action",
                      rating=4.5,
                      year=2009
                      )
        result = add_movie(movie)
        self.assertEqual(200, result)

    def test_update_movie(self):
        movie = Movie(name="Transformers",
                      actors="Peter Cullen, Hugo Weaving, Mark Ryan, Robert Foxworth, Jess Harnell, Charlie Adler, "
                             "Darius McCrary, Reno Wilson, Jimmie Wood",
                      director="James Cameron",
                      genre="Science fiction, Action",
                      rating=4.3,
                      year=2009
                      )
        movie_name = "Transformers"
        result = update_movie(movie_name, movie)
        movie_updated = result
        self.assertEqual(2009, movie_updated["year"])

    def test_delete_movie_by_name(self):
        name_movie = "Avatar"
        result = delete_movie_by_name(name_movie)
        self.assertEqual(204, result)


if __name__ == '__main__':
    unittest.main()
