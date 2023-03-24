from fastapi import FastAPI,APIRouter
import models
from database import engine

from router import orders,owner,menucard


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(orders.router)
app.include_router(owner.router)
app.include_router(menucard.router)