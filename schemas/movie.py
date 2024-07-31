def movie_schema(item) -> dict:
    return {
        "name": item["name"],
        "actors": item["actors"],
        "director": item["director"],
        "genre": item["genre"],
        "rating": float(item["rating"]),
        "year": int(item["year"]),
    }


def movies_schema(entity) -> list:
    return [movie_schema(item)for item in entity]
