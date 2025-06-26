from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    category_id: str 
    description: Optional[str] = ""
    stock: int
    images: Optional[List[str]] = []

class ProductResponse(BaseModel):
    id: str
    name: str
    price: float
    category: dict  # Assuming category is a dict with id and name
    description: Optional[str]
    stock: int
    images: List[str]
