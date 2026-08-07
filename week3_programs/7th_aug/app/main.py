from fastapi import FastAPI

from app.database import engine, Base

from app.routes.customer import router as customer_router


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Online Game Customer Review API")


app.include_router(customer_router)
