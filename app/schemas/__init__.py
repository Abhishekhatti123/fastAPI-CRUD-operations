from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True