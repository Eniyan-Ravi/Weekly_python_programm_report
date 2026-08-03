#delete_game
from fastapi import APIRouter
from app.database import GAMES

router = APIRouter()


@router.delete("/games/{game_id}")
async def delete_game(game_id: int):

    for game in GAMES:

        if game.id == game_id:

            GAMES.remove(game)

            return {
                "message": "Game Deleted Successfully"
            }

    return {
        "message": "Game not found"
    }