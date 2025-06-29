from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItemSchema(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float

class CreateOrder(BaseModel):
    shipping_address: str

class OrderResponse(BaseModel):
    id: str
    user_id: str
    items: List[OrderItemSchema]
    total_price: float
    shipping_address: str
    status: str
    created_at: datetime
