from bson import ObjectId
from core.database import db
from models.wishlist_model import wishlist_item_helper
from datetime import datetime

async def add_to_wishlist(user_id: str, product_id: str):
    exists = await db.wishlist.find_one({
        "user_id": ObjectId(user_id),
        "product_id": ObjectId(product_id)
    })
    if exists:
        return {"message": "Already in wishlist"}

    await db.wishlist.insert_one({
        "user_id": ObjectId(user_id),
        "product_id": ObjectId(product_id),
        "created_at": datetime.utcnow()
    })
    return {"message": "Added to wishlist"}

async def get_user_wishlist(user_id: str):
    items = db.wishlist.find({"user_id": ObjectId(user_id)})
    return [await wishlist_item_helper(item) async for item in items]

async def remove_from_wishlist(user_id: str, product_id: str):
    result = await db.wishlist.delete_one({
        "user_id": ObjectId(user_id),
        "product_id": ObjectId(product_id)
    })
    if result.deleted_count:
        return {"message": "Removed from wishlist"}
    return {"message": "Item not found in wishlist"}
async def clear_wishlist(user_id: str):
    result = await db.wishlist.delete_many({"user_id": ObjectId(user_id)})
    if result.deleted_count:
        return {"message": "Wishlist cleared"}
    return {"message": "No items to clear in wishlist"}     