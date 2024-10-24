from fastapi import APIRouter, HTTPException
from ..utils import get, set
from components.game.service import get_present
from fastapi.responses import FileResponse
import time
import os

router = APIRouter(prefix="/game", tags=["Game"])

@router.post("/presents")
async def presents(id: int, username: str, name: str):
    # Ключ для хранения времени последнего вызова

    # Получаем время последнего вызова из Redis
    last_call_time = await get(id)

    current_time = time.time()  # Текущее время в секундах

    # Если last_call_time не None, проверяем разницу во времени
    if last_call_time is not None:
        time_since_last_call = current_time - float(last_call_time)
        # Если прошло меньше 24 часов (86400 секунд), возвращаем ошибку
        if time_since_last_call < 24 * 60 * 60:
            raise HTTPException(status_code=403, detail="Вы можете вызывать эту функцию только раз в 24 часа.")

    # Сохраняем текущее время как время последнего вызова
    await set(id, username, current_time)


    # Получаем и возвращаем подарок
    return await get_present(id, username, name)


@router.get("/time")
async def timer(id: int):
    # Ключ для хранения времени последнего вызова

        # Получаем время последнего вызова из Redis
    try:
        last_call_time = await get(id)
        return int(24 * 60 * 60 - (int(time.time()) - int(last_call_time)))
    except Exception as _ex:
        return 0

@router.get("/img/{name}")
async def img(name: str):
    p = os.path.join("imageItem", name)
    return FileResponse(p)
