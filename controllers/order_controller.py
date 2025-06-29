from bson import ObjectId
from datetime import datetime
from core.database import db

async def place_order(user_id: str, shipping_address: str):
    cart_items = await db.cart_items.find({"user_id": ObjectId(user_id)}).to_list(length=None)

    if not cart_items:
        raise Exception("Your cart is empty.")

    order_items = []
    total_price = 0

    for item in cart_items:
        product = await db.products.find_one({"_id": ObjectId(item["product_id"])})
        if not product:
            raise Exception("Product not found.")
        if product["stock"] < item["quantity"]:
            raise Exception(f"Not enough stock for {product['name']}")

        await db.products.update_one(
            {"_id": ObjectId(item["product_id"])},
            {"$inc": {"stock": -item["quantity"]}}
        )

        order_items.append({
            "product_id": str(item["product_id"]),
            "name": product["name"],
            "quantity": item["quantity"],
            "price": product["price"]
        })

        total_price += product["price"] * item["quantity"]

    order = {
        "user_id": ObjectId(user_id),
        "items": order_items,
        "total_price": total_price,
        "shipping_address": shipping_address,
        "status": "Pending",
        "created_at": datetime.utcnow()
    }

    result = await db.orders.insert_one(order)
    await db.cart_items.delete_many({"user_id": ObjectId(user_id)})

    order["id"] = str(result.inserted_id)
    order["user_id"] = str(order["user_id"])
    return order

async def get_user_orders(user_id: str):
    orders = await db.orders.find({"user_id": ObjectId(user_id)}).to_list(length=None)
    for o in orders:
        o["id"] = str(o["_id"])
        o["user_id"] = str(o["user_id"])
    return orders

async def get_all_orders():
    orders = await db.orders.find().to_list(length=None)
    for o in orders:
        o["id"] = str(o["_id"])
        o["user_id"] = str(o["user_id"])
    return orders

async def update_order_status(order_id: str, status: str):
    result = await db.orders.update_one(
        {"_id": ObjectId(order_id)},
        {"$set": {"status": status}}
    )
    if result.modified_count:
        return {"message": "Order status updated"}
    return {"error": "Failed to update status"}
