from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import Owner
from passlib.context import CryptContext


router = APIRouter(
    prefix="/owner",
    tags=['owner']
)
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hashed(password):
    return bcrypt_context.hash(password)


@router.get("/allOwnerList")
async def allOwnerList(db:Session  = Depends(get_db)):
    all = db.query(models.Owner).all()
    return all


@router.post("/createOwner")
async def createOnwer(owner:Owner,db:Session = Depends(get_db)):
    owner_model = models.Owner()
    owner_model.ownerId = owner.ownerId
    owner_model.ownerName = owner.ownerName
    owner_model.ownerEmail = owner.ownerEmail
    owner_model.ownerPassword = get_password_hashed(owner.ownerPassword)
    owner_model.ownerVentureName = owner.ownerVentureName
    owner_model.ownerVentureType = owner.ownerVentureType
    owner_model.ownerAddress = owner.ownerAddress

    db.add(owner_model)
    db.commit()
    return{"success":200}
