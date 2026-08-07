from fastapi import FastAPI
from practice.item_routes import router as item_router

app=FastAPI()

app.include_router(item_router)