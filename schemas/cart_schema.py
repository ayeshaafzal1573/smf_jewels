from pydantic import BaseModel, Field
from typing import Optional

class AddCartItem(BaseModel):
    product_id: str
    quantity: int = Field(..., gt=0)

class UpdateCartItem(BaseModel):
    quantity: int = Field(..., gt=0)