#update_game
from fastapi import APIRouter
from app.database import GAMES
from app.schemas import GameRequest

router = APIRouter()


@router.put("/games/{game_id}")
async def update_game(game_id: int, game_request: GameRequest):

    for game in GAMES:

        if game.id == game_id:

            game.name = game_request.name
            game.genre = game_request.genre
            game.developer = game_request.developer
            game.description = game_request.description
            game.rating = game_request.rating
            game.price = game_request.price

            return {
                "message": "Game Updated Successfully",
                "game": game.to_dict()
            }

    return {"message": "Game not found"}

