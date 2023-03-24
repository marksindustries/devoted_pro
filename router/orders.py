from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import CreateOrders


router = APIRouter(
    prefix='/order',
    tags=['orders']
)


@router.get("/getAllOrders")
async def getAllOrders(db:Session = Depends(get_db)):
    all = db.query(models.Orders).all()
    return all


@router.post("/createOrder")
async def createAllOrders(order:CreateOrders,db:Session=Depends(get_db)):
    order_model = models.Orders()
    order_model.ownerId = order.ownerId
    order_model.customerOccassion = order.customerOccassion
    order_model.customerSegmentation = order.customerSegmentation

    db.add(order_model)
    db.commit()

    return {"success":200}
