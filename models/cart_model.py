from bson import ObjectId

def cart_item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "user_id": str(item["user_id"]),
        "product_id": str(item["product_id"]),
        "quantity": item["quantity"]
    }
