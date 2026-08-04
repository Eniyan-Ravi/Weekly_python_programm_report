#search_by_rating
from fastapi import APIRouter
from app.database import GAMES

router = APIRouter()


@router.get("/games/search/rating/")
async def search_game_by_rating(rating: float):

    games = []

    for game in GAMES:

        if game.rating >= rating:

            games.append(game.to_dict())

    if len(games) == 0:

        return {
            "message": "No games found"
        }

    return games