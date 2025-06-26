def category_helper(category) -> dict:
    return {
        "id": str(category["_id"]),
        "name": category["name"],
        "slug": category["slug"],
        "image": category.get("image", None),
    }
def category_helper_list(categories) -> list:
    return [category_helper(category) for category in categories]