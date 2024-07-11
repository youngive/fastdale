from fastapi import APIRouter, Request, Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from src.controllers.users import authenticate_user, register_user, get_cabinet_json
from src.models.database import get_db
from src.models.user import User
from src.schemes.user import UserBase
from src.utilities.generate import generate_ticket
import src.utilities.config as cfg
from src.utilities.const import Const as cst
from src.utilities.network import is_local_network, check_for_updates

router = APIRouter()

# Создайте объект Jinja2Templates и укажите путь к папке с шаблонами
templates = Jinja2Templates(directory="assets/templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    if request.session.get("userId", None) is not None:
        return RedirectResponse(url="/game", status_code=303)
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
async def root(request: Request, form: UserBase = Depends(UserBase.as_form), db: Session = Depends(get_db)):
    try:
        user_data = UserBase(USERNAME=form.USERNAME, PASSWORD=form.PASSWORD)
        ticket = generate_ticket()
        user, error = authenticate_user(db, user_data.USERNAME, user_data.PASSWORD, ticket)
        if user is None and error is not None:
            return templates.TemplateResponse(
                request=request, name="index.html", context={"error": error}
            )
        if user is not None and error is None:
            request.session["userId"] = user.ID
            request.session["ticket"] = ticket
            request.session["roleflags"] = user.ROLEFLAGS
            return RedirectResponse(url="/game", status_code=303)
    except ValidationError as e:
        type = str(e.errors()[0]['type'])
        if type == 'string_too_short':
            error = "Короткий логин или пароль"
        elif type == "string_too_long":
            error = "Длинный логин или пароль"
        elif type == "string_pattern_mismatch":
            error = "Недопустимые символы в логине или пароле"
        else:
            error = type
        return templates.TemplateResponse("index.html", {"request": request, "error": error})


@router.get("/register", response_class=HTMLResponse)
async def route_register(request: Request):
    if request.session.get("userId", None) is not None:
        return RedirectResponse(url="/game", status_code=303)
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register", response_class=HTMLResponse)
async def route_register(request: Request, form: UserBase = Depends(UserBase.as_form), db: Session = Depends(get_db)):
    try:
        user_data = UserBase(USERNAME=form.USERNAME, PASSWORD=form.PASSWORD)
        ticket = generate_ticket()
        userId, error = register_user(db, user_data.USERNAME, user_data.PASSWORD, ticket)
        if userId is None and error is not None:
            return templates.TemplateResponse(
                request=request, name="register.html", context={"error": error}
            )
        if userId is not None and error is None:
            request.session["userId"] = userId
            request.session["ticket"] = ticket
            request.session["roleflags"] = 2
            return RedirectResponse(url="/game", status_code=303)
    except ValidationError as e:
        type = str(e.errors()[0]['type'])
        if type == 'string_too_short':
            error = "Короткий логин или пароль"
        elif type == "string_too_long":
            error = "Длинный логин или пароль"
        elif type == "string_pattern_mismatch":
            error = "Недопустимые символы в логине или пароле"
        else:
            error = type
        return templates.TemplateResponse("register.html", {"request": request, "error": error})


@router.get("/game", response_class=HTMLResponse)
async def route_game(request: Request, db: Session = Depends(get_db)):
    if request.session.get("userId", None) is None:
        return RedirectResponse(url="/")

    user_id = request.session.get("userId")
    user = db.query(User).filter(User.ID == user_id).first() if user_id else None

    # Проверяем соответствие тикета пользователя
    if user and request.session.get("ticket") != user.TICKET:
        # Если тикеты не совпадают, деавторизуем пользователя
        return RedirectResponse(url="/logout")

    return templates.TemplateResponse("game.html",
                                      {"request": request, "webhost": cfg.webhost, "webport": cfg.webport})


@router.get("/cabinet", response_class=HTMLResponse)
async def route_game(request: Request, db: Session = Depends(get_db)):
    if request.session.get("userId", None) is None:
        return RedirectResponse(url="/")

    user_id = request.session.get("userId")
    user = db.query(User).filter(User.ID == user_id).first() if user_id else None

    # Проверяем соответствие тикета пользователя
    if user and request.session.get("ticket") != user.TICKET:
        # Если тикеты не совпадают, деавторизуем пользователя
        return RedirectResponse(url="/logout")

    json = get_cabinet_json(db, request)
    return templates.TemplateResponse("cabinet.html", json)


@router.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    # Проверяем наличие ключей в сессии и удаляем их
    if "userId" in request.session:
        del request.session["userId"]
    if "ticket" in request.session:
        del request.session["ticket"]
    if "roleflags" in request.session:
        del request.session["roleflags"]

    return RedirectResponse(url="/", status_code=303)
