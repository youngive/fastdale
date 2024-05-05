from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from src.controllers.users import add_money_controller
from src.models.database import get_db
from src.schemes.request import CurrencyRequest
from src.utilities.network import is_local_network

router = APIRouter()


@router.post("/addMoney.php", status_code=200)
async def add_money(request: Request, form: CurrencyRequest = Depends(CurrencyRequest.as_form),
                    db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return add_money_controller(db, ticket=form.ticket, amount=form.amount)
