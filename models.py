from sqlalchemy.orm import Session,relationship
from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from database import Base



class Owner(Base):
    __tablename__ = "owner"
    ownerId = Column(String,primary_key=True)
    ownerName = Column(String)
    ownerAddress = Column(String)
    ownerEmail = Column(String)
    ownerVentureType = Column(String)
    ownerVentureName = Column(String)
    ownerPassword = Column(String)

    order = relationship("Orders",back_populates='owner')
    menucard = relationship("MenuCard",back_populates="owner")

class MenuCard(Base):
    __tablename__ = 'menucard'
    menuItemNo = Column(Integer,primary_key=True,index=True)
    ownerId = Column(Integer,ForeignKey('owner.ownerId'))
    itemName = Column(String)
    itemId = Column(Integer)
    itemPrice = Column(Integer)
    itemCategory = Column(String)

    owner = relationship("Owner",back_populates='menucard')



class Orders(Base):
    __tablename__ = "orders"
    ownerId = Column(String,ForeignKey('owner.ownerId'))
    orderNo = Column(String,primary_key=True,index=True)
    orderList = Column(String)
    customerSegmentation = Column(String)
    customerOccassion = Column(String)
    time = Column(String)

    owner = relationship("Owner",back_populates="order")

