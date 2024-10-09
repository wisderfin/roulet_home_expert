from fastapi import APIRouter


from components.service import DEPENDS
from components.game.service import get_present
from components.game.scheme import DepositScheme
from components.auth.scheme import IdScheme

router = APIRouter(prefix="/game", tags=["Game"])


@router.post("/presents", dependencies=DEPENDS)
async def presents(deposit: DepositScheme, user: IdScheme):
    return await get_present(deposit.deposit)
