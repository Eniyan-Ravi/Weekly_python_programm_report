from fastapi import FastAPI

from app.database import engine, Base

from app.routes.categories import router as category

from app.routes.users import router as users

from app.routes.payment_methods import router as payment_method

from app.routes.subscriptions import router as subscription

from app.routes.emis import router as emi

from app.routes.payment_history import router as payment_history


app = FastAPI(title="Subscription and EMI tracker")

app.include_router(users)
app.include_router(category)
app.include_router(payment_method)
app.include_router(subscription)
app.include_router(emi)
app.include_router(payment_history)



Base.metadata.create_all(bind=engine)