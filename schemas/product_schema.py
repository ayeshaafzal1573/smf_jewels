from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    category: str
    description: Optional[str] = ""
    stock: int
    images: Optional[List[str]] = []

class ProductResponse(BaseModel):
    id: str
    name: str
    price: float
    category: str
    description: Optional[str]
    stock: int
    images: List[str]
