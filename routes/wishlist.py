from fastapi import APIRouter, Depends
from core.deps import get_current_user
from controllers.wishlist_controller import *

router = APIRouter(prefix="/api/wishlist", tags=["Wishlist"])

@router.get("/")
async def get_wishlist(user: dict = Depends(get_current_user)):
    return await get_user_wishlist(user["id"])

@router.post("/add-to-wishlist/{product_id}")
async def add_to_user_wishlist(product_id: str, user: dict = Depends(get_current_user)):
    return await add_to_wishlist(user["id"], product_id)

@router.delete("/delete-from-wishlist/{product_id}")
async def delete_from_wishlist(product_id: str, user: dict = Depends(get_current_user)):
    return await remove_from_wishlist(user["id"], product_id)