from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter()

@router.post("/async/Ping", response_class=HTMLResponse)
async def ping():
    return "<response isPong=\"true\" />"