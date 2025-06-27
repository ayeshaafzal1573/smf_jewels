from bson import ObjectId
from core.database import db
from models.cart_model import cart_item_helper

async def get_user_cart(user_id: str):
    cart_items = db.cart.find({"user_id": ObjectId(user_id)})
    return [cart_item_helper(item) async for item in cart_items]

from bson import ObjectId
from core.database import db
from fastapi import HTTPException

async def add_to_cart(user_id: str, data: dict):
    product_id = data["product_id"]
    quantity = data["quantity"]

    product = await db.products.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if quantity > product["stock"]:
        raise HTTPException(status_code=400, detail="Requested quantity exceeds available stock")

    existing = await db.cart_items.find_one({
        "user_id": ObjectId(user_id),
        "product_id": ObjectId(product_id)
    })

    if existing:
        new_quantity = existing["quantity"] + quantity
        if new_quantity > product["stock"]:
            raise HTTPException(status_code=400, detail="Total quantity exceeds available stock")

        await db.cart_items.update_one(
            {"_id": existing["_id"]},
            {"$set": {"quantity": new_quantity}}
        )
    else:
        await db.cart_items.insert_one({
            "user_id": ObjectId(user_id),
            "product_id": ObjectId(product_id),
            "quantity": quantity
        })

    return {"message": "Item added to cart"}

async def update_cart_item(user_id: str, product_id: str, quantity: int):
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if quantity > product["stock"]:
        raise HTTPException(status_code=400, detail="Requested quantity exceeds available stock")

    result = await db.cart_items.update_one(
        {
            "user_id": ObjectId(user_id),
            "product_id": ObjectId(product_id)
        },
        {"$set": {"quantity": quantity}}
    )

    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Cart item not found")

    return {"message": "Cart updated"}

async def remove_from_cart(user_id: str, product_id: str):
    await db.cart.delete_one({
        "user_id": ObjectId(user_id),
        "product_id": ObjectId(product_id)
    })
    return {"msg": "Item removed"}
