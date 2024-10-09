from sqlalchemy import select

from components.database import get_async_session as connect
from components.game.model import PresentModel
from components.auth.model import UserModel
from components.auth.utils import get_user

async def get_all_presents():
    async for session in connect():
        presents = await session.execute(select(PresentModel))
        result = presents.scalars().all()
        await session.close()
        return result


