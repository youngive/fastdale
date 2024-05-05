from fastapi import APIRouter, Depends, Query, Request, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import PlainTextResponse

from src.utilities.network import is_local_network
from src.views.users import get_user_data_view
from src.models.database import get_db

router = APIRouter()


@router.get("/kek.php", response_class=PlainTextResponse)
async def get_user_data(request: Request, ticket: str = Query(...), db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return get_user_data_view(db, ticket=ticket)
