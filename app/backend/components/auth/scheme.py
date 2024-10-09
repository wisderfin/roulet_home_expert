from pydantic import BaseModel


class IdScheme(BaseModel):
    id: int


class UserScheme(IdScheme):
    username: str

class UserBalanceScheme(IdScheme):
    change_balance: float
