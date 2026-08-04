#get_games
from fastapi import APIRouter
from app.database import GAMES

router = APIRouter()


@router.get("/games")
async def get_all_games():
    return [game.to_dict() for game in GAMES]


@router.get("/games/{game_id}")
async def get_game_by_id(game_id: int):

    for game in GAMES:

        if game.id == game_id:
            return game.to_dict()

    return {"message": "Game not found"}