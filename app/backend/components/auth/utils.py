from sqlalchemy import select

from components.database import get_async_session as connect
from components.auth.model import UserModel
from components.auth.errors import user_already_exists, user_not_found

async def get_user(id: int):
    async for session in connect():
        user = await session.execute(select(UserModel).where(UserModel.id == id))
        result = user.scalars().first()
        if result:
            await session.close()
            return result
        raise user_not_found


async def create_user(id: int, username: str):
    check_user = await get_user(id)
    if not check_user:
        async for session in connect():
            user = UserModel(id=id, username=username)
            session.add(user)
            await session.commit()
            await session.close()
        return user
    raise user_already_exists

async def blocked_user(id: int):
    async for session in connect():
        user = await get_user(id)
        if user:
            user.blocked = True
            await session.commit()
            await session.close()
            return user
        raise user_not_found

async def unblocked_user(id: int):
    async for session in connect():
        user = await get_user(id)
        if user:
            user.blocked = False
            await session.commit()
            await session.close()
            return user
        raise user_not_found

async def get_user_balance(id: int):
    user = await get_user(id)
    balance = user.balance
    return balance

async def edit_user_balance(id: int, balance: float):
    async for session in connect():
        user = await get_user(id)
        curent_balance = float(user.balance)
        curent_balance += balance
        user.balance = curent_balance
        session.add(user)
        await session.commit()
