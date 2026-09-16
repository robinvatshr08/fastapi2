from pydantic import BaseModel

class ProductDTO(BaseModel):
    id:int
    price:int = 0
    count: int = 0
    brand:str
    title:str
    

