from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from src.controllers.users import update_money_controller
from src.models.database import get_db
from src.schemes.request import MoneyRequest
from src.utilities.network import is_local_network

router = APIRouter()


@router.post("/money.php", status_code=200)
async def update_money(request: Request, form: MoneyRequest = Depends(MoneyRequest.as_form),
                       db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return update_money_controller(db, ticket=form.ticket, priceRu=form.priceRu, priceSm=form.priceSm)
