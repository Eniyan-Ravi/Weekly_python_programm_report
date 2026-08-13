from fastapi import FastAPI

from app.routes.http_exception import router as http_router
from app.routes.path_validation import router as path_router
from app.routes.query_validation import router as query_router
from app.routes.status_code import router as status_router


app = FastAPI(
    title="Validation Practice API"
)

app.include_router(http_router)
app.include_router(path_router)
app.include_router(query_router)
app.include_router(status_router)