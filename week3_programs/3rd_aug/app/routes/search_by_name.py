#search_by_name
from fastapi import APIRouter
from app.database import GAMES

router = APIRouter()


@router.get("/games/name/{game_name}")
async def search_by_name(game_name: str):

    for game in GAMES:

        if game.name.lower() == game_name.lower():
            return game.to_dict()

    return {"message": "Game Not Found"}