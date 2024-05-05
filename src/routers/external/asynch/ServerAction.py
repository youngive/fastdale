from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request

from src.controllers.users import server_action_controller
from src.models.database import get_db

router = APIRouter()


@router.post("/async/ServerAction")
async def route_action(request: Request, db: Session = Depends(get_db)):
    if request.session.get("userId", None) is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return server_action_controller(db, request)
