from bson import ObjectId
from core.database import db

async def product_helper(product) -> dict:
    # 🛠 Use the correct key: category_id
    category = await db.categories.find_one({
        "_id": ObjectId(product["category_id"])
    })
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "description": product.get("description", ""),
        "stock": product["stock"],
        "images": product.get("images", []),
        "category": {
            "id": str(category["_id"]),
            "name": category["name"],
            "slug": category["slug"]
        } if category else None
    }

