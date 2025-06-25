from fastapi import APIRouter, HTTPException
from core.database import db
from models.product_model import product_helper
from schemas.product_schema import ProductCreate, ProductResponse
from typing import List
from bson import ObjectId

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
async def get_all_products():
    products = []
    async for product in db.products.find():
        products.append(product_helper(product))
    return products

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_helper(product)
