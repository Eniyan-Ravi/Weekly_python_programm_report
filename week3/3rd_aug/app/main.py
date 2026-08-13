#main
from fastapi import FastAPI

from app.routes.get_games import router as get_router
from app.routes.create_game import router as create_router
from app.routes.update_game import router as update_router
from app.routes.delete_game import router as delete_router
from app.routes.search_by_name import router as search_name_router
from app.routes.search_by_rating import router as search_rating_router


app = FastAPI(
    title="Game Library API"
)


app.include_router(get_router)
app.include_router(create_router)
app.include_router(update_router)
app.include_router(delete_router)
app.include_router(search_name_router)
app.include_router(search_rating_router)