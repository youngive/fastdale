from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from src.controllers.users import set_avatar_controller
from src.models.database import get_db
from src.schemes.request import AvaRequest
from src.utilities.network import is_local_network

router = APIRouter()


@router.post("/setAvatar.php", status_code=200)
async def set_avatar(request: Request, form: AvaRequest = Depends(AvaRequest.as_form), db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return set_avatar_controller(db, ticket=form.ticket, avatar=form.avatar)
