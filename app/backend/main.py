from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from components.game.router import router as game_router


app = FastAPI()

origins = ['https://locfront.ru.tuna.am', 'https://locfronta.ru.tuna.am']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


app.include_router(game_router)
