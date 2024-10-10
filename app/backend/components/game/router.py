from fastapi import APIRouter, HTTPException
from ..redis_utils import get, set
from components.game.service import get_present
import time

router = APIRouter(prefix="/game", tags=["Game"])

@router.post("/presents")
async def presents(id: int, username: str):
    # Ключ для хранения времени последнего вызова
    key = f"user:{id}:last_present_call"

    # Получаем время последнего вызова из Redis
    last_call_time = get(key)

    current_time = time.time()  # Текущее время в секундах

    # Если last_call_time не None, проверяем разницу во времени
    if last_call_time is not None:
        time_since_last_call = current_time - float(last_call_time)
        # Если прошло меньше 24 часов (86400 секунд), возвращаем ошибку
        if time_since_last_call < 3:
            raise HTTPException(status_code=403, detail="Вы можете вызывать эту функцию только раз в 24 часа.")

    # Сохраняем текущее время как время последнего вызова
    set(key, current_time)


    # Получаем и возвращаем подарок
    return await get_present(id, username)


@router.get("/time")
async def timer(id: int):
    # Ключ для хранения времени последнего вызова
    key = f"user:{id}:last_present_call"

        # Получаем время последнего вызова из Redis
    try:
        last_call_time = get(key)
        return int(3 - (int(time.time()) - float(last_call_time)))
    except Exception as _ex:
        return 0
