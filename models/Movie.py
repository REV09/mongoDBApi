from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    actors: str
    director: str
    genre: str
    rating: float
    year: int
