from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from random import randint

from components.game.router import router as game_router
from components.service import DEPENDS, verify_ip, verify_user_agent

app = FastAPI()

origins = ['https://slmnfrontend.ru.tuna.am', '*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)




@app.get('/test', dependencies=[Depends(verify_ip), Depends(verify_user_agent)])
async def main(request: Request):
    # sleep(3)
    return [randint(0, 100) for _ in range(0, 20)]

app.include_router(game_router)
