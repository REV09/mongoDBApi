from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routes.movies_routes import routes_movies
from routes.auth_routes import auth_routes
from dotenv import load_dotenv

app = FastAPI(
    title="MongoDB Project",
    description="A simple API for interacting with MongoDB database",
    openapi_tags=[{
        "name": "movies",
        "description": "Movies API for interacting with MongoDB database"
    }],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv('.env')
app.include_router(auth_routes)
app.include_router(routes_movies)
