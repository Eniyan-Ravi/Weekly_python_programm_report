from fastapi import FastAPI

from app.routes.query_parameter import router as query_router
from app.routes.path_parameter import router as path_router
from app.routes.update_student import router as update_router
from app.routes.delete_student import router as delete_router

app = FastAPI(
    title="Student Management API"
)

app.include_router(query_router)
app.include_router(path_router)
app.include_router(update_router)
app.include_router(delete_router)