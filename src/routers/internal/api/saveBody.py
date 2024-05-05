from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from src.controllers.users import save_body_controller
from src.models.database import get_db
from src.schemes.request import BodyRequest
from src.utilities.network import is_local_network

router = APIRouter()


@router.post("/saveBody.php", status_code=200)
async def save_body(request: Request, form: BodyRequest = Depends(BodyRequest.as_form), db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return save_body_controller(db, ticket=form.ticket, body_color=form.body_color, ears_color=form.ears_color,
                                ears=form.ears, eyes=form.eyes, horns=form.horns, legs=form.legs,
                                legs_color=form.legs_color, mouth=form.mouth, nose=form.nose, peak=form.peak)
