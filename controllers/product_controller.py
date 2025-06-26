from core.database import db
from bson import ObjectId
from datetime import datetime
from models.product_model import product_helper
# Create product
async def create_product(data: dict):
    data["created_at"] = datetime.utcnow()
    result = await db.products.insert_one(data)
    new_product = await db.products.find_one({"_id": result.inserted_id})
    return product_helper(new_product)
# Update product by ID
async def update_product(product_id: str, data: dict):
    updated = await db.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": data}
    )
    if updated.modified_count == 0:
        return None
    return await db.products.find_one({"_id": ObjectId(product_id)})
# Delete product by ID
async def delete_product(product_id: str):
    deleted = await db.products.delete_one({"_id": ObjectId(product_id)})
    return deleted.deleted_count > 0

# Get all products
async def get_all_products():
    return await db.products.find().to_list(length=100)
# Get product by ID
async def get_product_by_id(product_id: str):
    if not ObjectId.is_valid(product_id):
        return None
    return await db.products.find_one({"_id": ObjectId(product_id)})