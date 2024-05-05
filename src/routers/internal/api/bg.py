from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from src.controllers.users import update_bg_controller
from src.models.database import get_db
from src.schemes.request import BgRequest
from src.utilities.network import is_local_network

router = APIRouter()


@router.post("/bg.php", status_code=200)
async def update_bg(request: Request, form: BgRequest = Depends(BgRequest.as_form), db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return update_bg_controller(db, ticket=form.ticket, bg=form.bg)
