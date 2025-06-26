from models.category_model import category_helper
from bson import ObjectId
from core.database import db

async def product_helper(product) -> dict:
    category = await db.categories.find_one({"_id": ObjectId(product["category_id"])})
    
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "description": product.get("description", ""),
        "stock": product["stock"],
        "images": product.get("images", []),
        "category": category_helper(category) if category else None
    }