from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import MenuCard



router = APIRouter(
    prefix='/MenuCard',
    tags=['Menu Card']
)


@router.get('/getAll')
async def getAllItems(db:Session = Depends(get_db)):
    all = db.query(models.MenuCard).all()
    return all


@router.post('/createMenu')
async def createMenu(menu:MenuCard,db:Session = Depends(get_db)):
    menu_model = models.MenuCard()

    menu_model.ownerId = menu.ownerId
    menu_model.itemId = menu.itemId
    menu_model.itemName = menu.itemName
    menu_model.itemCategory = menu.itemCategory
    menu_model.itemPrice = menu.itemPrice

    db.add(menu_model)
    db.commit()
    return {"success":200}
