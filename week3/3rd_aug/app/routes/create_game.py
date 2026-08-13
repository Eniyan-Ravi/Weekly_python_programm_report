#create_game
from fastapi import APIRouter
from app.database import GAMES
from app.model import Game
from app.schemas import GameRequest

router = APIRouter()


def generate_game_id(game: GameRequest):

    if len(GAMES) > 0:
        game.id = GAMES[-1].id + 1
    else:
        game.id = 1

    return game


@router.post("/games")
async def create_game(game_request: GameRequest):

    game_request = generate_game_id(game_request)

    new_game = Game(**game_request.model_dump())

    GAMES.append(new_game)

    return {
        "message": "Game Added Successfully",
        "game": new_game.to_dict()
    }