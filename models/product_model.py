def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "category": product["category"],
        "description": product.get("description", ""),
        "stock": product["stock"],
        "images": product.get("images", []),
    }
