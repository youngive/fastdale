from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from src.controllers.users import update_bg_inventory_controller
from src.models.database import get_db
from src.schemes.request import InvRequest
from src.utilities.network import is_local_network

router = APIRouter()


@router.post("/bginv.php", status_code=200)
async def update_bg_inventory(request: Request, form: InvRequest = Depends(InvRequest.as_form),
                              db: Session = Depends(get_db)):
    if not is_local_network(request):
        raise HTTPException(status_code=403, detail="Forbidden")
    return update_bg_inventory_controller(db, ticket=form.ticket, inventory=form.inventory)
