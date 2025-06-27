from fastapi import APIRouter, Depends, HTTPException
from schemas.cart_schema import AddCartItem, UpdateCartItem
from controllers.cart_controller import *
from core.deps import get_current_user

router = APIRouter(prefix="/api/cart", tags=["Cart"])


def block_admin(user):
    if user["role"] == "admin":
        raise HTTPException(status_code=403, detail="Admins are not allowed to use cart")
    return user


@router.get("/")
async def get_cart(user: dict = Depends(get_current_user)):
    block_admin(user)
    return await get_user_cart(user["id"])


@router.post("/")
async def add_item(data: AddCartItem, user: dict = Depends(get_current_user)):
    block_admin(user)
    return await add_to_cart(user["id"], data.dict())


@router.put("/update-cart/{product_id}")
async def update_item(product_id: str, data: UpdateCartItem, user: dict = Depends(get_current_user)):
    block_admin(user)
    return await update_cart_item(user["id"], product_id, data.quantity)


@router.delete("/remove-from-cart/{product_id}")
async def delete_item(product_id: str, user: dict = Depends(get_current_user)):
    block_admin(user)
    return await remove_from_cart(user["id"], product_id)
