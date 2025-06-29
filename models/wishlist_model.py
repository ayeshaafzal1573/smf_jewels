from bson import ObjectId
from core.database import db
from models.product_model import product_helper

async def wishlist_item_helper(item):
    product = await db.products.find_one({"_id": item["product_id"]})
    return await product_helper(product) if product else None
