from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from src.controllers.users import ban_user_controller
from src.models.database import get_db
from src.schemes.request import BanRequest
from src.utilities.network import is_local_network

router = APIRouter()


@router.post("/ban.php", status_code=200)
async def ban_user(request: Request, form: BanRequest = Depends(BanRequest.as_form), db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return ban_user_controller(db, ticket=form.ticket)
