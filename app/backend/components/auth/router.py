from fastapi import APIRouter, Depends

from components.auth.scheme import UserScheme, IdScheme, UserBalanceScheme
from components.auth.utils import create_user, get_user, blocked_user, unblocked_user
from components.auth.utils import edit_user_balance, get_user_balance
from components.auth.errors import user_not_found
from components.service import DEPENDS

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/create", dependencies=DEPENDS)
async def create(data: UserScheme):
    return await create_user(data.id, data.username)


@router.post("/get", dependencies=DEPENDS)
async def get(id: IdScheme):
    user = await get_user(id.id)
    if user:
        return user
    raise user_not_found

@router.post("/block", dependencies=DEPENDS)
async def block(id: IdScheme):
    return await blocked_user(id.id)


@router.post("/unblock", dependencies=DEPENDS)
async def unblock(id: IdScheme):
    return await unblocked_user(id.id)

@router.post("/balance", dependencies=DEPENDS)
async def balance(user: IdScheme):
    return {'balance': await get_user_balance(user.id)}

@router.post('/edit_balance', dependencies=DEPENDS)
async def edit_balance(balance: UserBalanceScheme):
    await edit_user_balance(balance.id, balance.change_balance)
