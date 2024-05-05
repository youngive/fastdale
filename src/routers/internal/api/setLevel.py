from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import PlainTextResponse

from src.controllers.users import set_level_controller
from src.models.database import get_db
from src.schemes.request import LvlRequest
from src.utilities.network import is_local_network

router = APIRouter()


@router.post("/setLevel.php", response_class=PlainTextResponse)
async def set_level(request: Request, form: LvlRequest = Depends(LvlRequest.as_form), db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return set_level_controller(db, id=form.id, level=form.level)
