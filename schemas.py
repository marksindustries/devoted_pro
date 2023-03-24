from pydantic import BaseModel

class Owner(BaseModel):
    ownerId :int
    ownerName :str
    ownerAddress :str
    ownerEmail :str
    ownerVentureType:str
    ownerVentureName :str
    ownerPassword :str



class CreateOrders(BaseModel):
    ownerId :int 
    customerSegmentation:str 
    customerOccassion :str
    


class MenuCard(BaseModel):
    ownerId:int 
    itemId:int
    itemName:str
    itemPrice:int
    itemCategory:str

