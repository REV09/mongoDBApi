from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from config.connection_db import get_connection
from bson import ObjectId
from schemas.movie import movie_schema, movies_schema
from models.Movie import Movie
from middlewares.verify_token_route import VerifyTokenRoute

routes_movies = APIRouter(route_class=VerifyTokenRoute)


@routes_movies.get("/movies", response_model=list[Movie], tags=["movies"])
def get_all_movies():
    connection = get_connection()
    result_set = connection.kuantikProject.movies.find()
    movies: list[Movie] = movies_schema(result_set)
    return movies


@routes_movies.get("/movies/{name_movie}", response_model=Movie, tags=["movies"])
def get_movie_by_name(name_movie: str):
    connection = get_connection()
    result = connection.kuantikProject.movies.find_one({"name": name_movie})
    if result is not None:
        movie = movie_schema(result)
        return movie

    else:
        raise HTTPException(status_code=404, detail="Movie not found")


@routes_movies.post("/movies", status_code=HTTP_200_OK, tags=["movies"])
def add_movie(movie: Movie):
    connection = get_connection()
    dict_movie = dict(movie)
    result = connection.kuantikProject.movies.insert_one(dict_movie).inserted_id
    if result is not None:
        new_movie = connection.kuantikProject.movies.find_one({"_id": ObjectId(result)})
        if new_movie:
            return HTTP_200_OK
        else:
            raise HTTPException(status_code=500 ,detail="Failed to get movie from database")

    else:
        raise HTTPException(status_code=500, detail="Failed to add movie to database")


@routes_movies.put("/movies/{name_movie}", response_model=Movie, tags=["movies"])
def update_movie(name_movie: str, movie: Movie):
    connection = get_connection()
    dict_movie = dict(movie)
    result = connection.kuantikProject.movies.update_one({"name": name_movie}, {"$set": dict_movie})
    if result is not None:
        movie_updated = get_movie_by_name(movie.name)
        if movie_updated:
            return movie_updated

        else:
            raise HTTPException(status_code=500, detail="Failed to get movie updated")

    else:
        raise HTTPException(status_code=500, detail="Failed to update movie")


@routes_movies.delete("/movies/{name_movie}", status_code=HTTP_204_NO_CONTENT, tags=["movies"])
def delete_movie_by_name(name_movie: str):
    connection = get_connection()
    result = connection.kuantikProject.movies.delete_one({"name": name_movie})
    if result:
        return HTTP_204_NO_CONTENT

    else:
        raise HTTPException(status_code=404, detail="Movie not found")
