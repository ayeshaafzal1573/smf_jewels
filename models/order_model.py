async def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": str(order["user_id"]),
        "items": [{"product_id": str(i["product_id"]), "quantity": i["quantity"]} for i in order["items"]],
        "shipping_address": order["shipping_address"],
        "total_price": order["total_price"],
        "status": order["status"],
        "created_at": order["created_at"]
    }
