from fastapi import APIRouter, HTTPException, Depends
from schemas.product_schema import ProductCreate, ProductResponse
from controllers.product_controller import (
    create_product, update_product, delete_product,
    get_all_products, get_product_by_id
)
from bson import ObjectId
from typing import List
from core.database import db
from models.product_model import product_helper
from core.deps import is_admin
router = APIRouter()

# ✅ POST /products (Admin Only)

@router.post("/add-product", response_model=ProductResponse)
async def add_product(product: ProductCreate, user=Depends(is_admin)):
    new_product = await create_product(product.dict())
    return new_product


# ✅ PUT /products/{id}
@router.put("/update-product/{product_id}", response_model=ProductResponse)
async def update(product_id: str, product: ProductCreate, user=Depends(is_admin)):
    updated = await update_product(product_id, product.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_helper(updated)

# ✅ DELETE /products/{id} 
@router.delete("/delete-product/{product_id}")
async def delete(product_id: str, user=Depends(is_admin)):
    deleted = await delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}



# ✅ GET /products — View all products (Public)
@router.get("/all", response_model=List[ProductResponse])
async def list_products():
    products = await get_all_products()

    result = []
    for p in products:
        item = await product_helper(p)  # ✅ Awaiting async helper
        result.append(item)

    return result
# ✅ GET /products/{product_id} — View single product by ID (Public)
@router.get("/products/{product_id}", response_model=ProductResponse)
async def view_product(product_id: str):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_helper(product)