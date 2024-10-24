from sqlalchemy import select

from components.database import get_async_session as connect
from model import UserModel

async def get(id: int):
    async for session in connect():
        user = await session.execute(select(UserModel).where(UserModel.id == id))
        result = user.scalars().first()
        if result:
            await session.close()
            return result.time
        return None


async def set(id: int, username: str, time: int):
    check_user = await get(id)
    if not check_user:
        async for session in connect():
            user = UserModel(id=id, username=username, time=time)
            session.add(user)
            await session.commit()
            await session.close()
        return user
