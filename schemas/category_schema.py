from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    name: str
    slug: str
    image: Optional[str] = None  # 👈 instead of icon

class CategoryResponse(BaseModel):
    id: str
    name: str
    slug: str
    image: Optional[str] = None
