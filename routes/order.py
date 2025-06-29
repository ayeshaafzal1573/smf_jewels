from fastapi import APIRouter, Depends, HTTPException
from schemas.order_schema import CreateOrder, OrderResponse
from typing import List
from controllers.order_controller import *
from core.deps import get_current_user, is_admin

router = APIRouter(prefix="/api/orders", tags=["Orders"])

@router.post("/place-order", response_model=OrderResponse)
async def create_order(data: CreateOrder, user: dict = Depends(get_current_user)):
    try:
        return await place_order(user["id"], data.shipping_address)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/all-orders", response_model=List[OrderResponse])
async def user_orders(user: dict = Depends(get_current_user)):
    return await get_user_orders(user["id"])

@router.get("/all-users-orders", response_model=List[OrderResponse])
async def admin_orders(_: dict = Depends(is_admin)):
    return await get_all_orders()

@router.put("/{order_id}/status")
async def update_status(order_id: str, status: str, _: dict = Depends(is_admin)):
    return await update_order_status(order_id, status)
