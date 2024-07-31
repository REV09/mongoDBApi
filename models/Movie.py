from pydantic import BaseModel, ValidationError


class Movie(BaseModel):
    name: str
    actors: str
    director: str
    genre: str
    rating: float
    year: int

    class Config:
        orm_mode = True
