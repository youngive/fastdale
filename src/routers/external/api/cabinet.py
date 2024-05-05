from fastapi import APIRouter, Depends, Request
from requests import Session
from starlette.responses import PlainTextResponse

from src.controllers.users import cabinet_controller
from src.models.database import get_db
from src.schemes.request import CabinetRequest

router = APIRouter(prefix="/api/external/cabinet")

@router.post("/handler", response_class=PlainTextResponse)
async def handle_cabinet_form(request: Request, form: CabinetRequest = Depends(CabinetRequest.as_form), db: Session = Depends(get_db)):
    level = form.level
    regday = form.regday
    regmonth = form.regmonth
    regyear = form.regyear
    return cabinet_controller(db, ticket=request.session.get("ticket"), level=level, regday=regday, regmonth=regmonth, regyear=regyear)
