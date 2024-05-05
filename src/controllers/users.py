import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.hash import md5_crypt

from starlette.requests import Request
from starlette.responses import PlainTextResponse

from src.models.user import User
from src.utilities.generate import generate_server_action_xml_str


def authenticate_user(db: Session, username: str, password: str, new_ticket: str):
    user = db.query(User).filter_by(USERNAME=username).first()
    if not user:
        return None, "Нет такого Смешарика"  # Пользователь не найден
    if md5_crypt.verify(password, user.PASSWORD):
        # Обновление билета пользователя
        user.TICKET = new_ticket
        db.commit()
        return user, None  # Успешная аутентификация
    return None, "Неправильный пароль"  # Неправильный пароль


def register_user(db: Session, username: str, password: str, new_ticket: str):
    user = db.query(User).filter_by(USERNAME=username).first()
    if user:
        return None, "Игрок с таким ником уже существует"  # Пользователь найден
    hashed_password = md5_crypt.hash(password)
    ava = "IsBodyPart>true|BodyPartTypeId>5|MediaResourceID>67|LayerID>25|BodyPartId>30|Id>30|Color>NaN;IsBodyPart>true|BodyPartTypeId>6|MediaResourceID>68|LayerID>39|BodyPartId>31|Id>31|Color>16762375;IsBodyPart>true|BodyPartTypeId>7|MediaResourceID>74|LayerID>29|BodyPartId>40|Id>40|Color>NaN;IsBodyPart>true|BodyPartTypeId>8|MediaResourceID>98|LayerID>49|BodyPartId>73|Id>73|Color>NaN;IsBodyPart>true|BodyPartTypeId>2|MediaResourceID>55|LayerID>9|BodyPartId>1|Id>1|Color>NaN;IsBodyPart>true|BodyPartTypeId>3|MediaResourceID>56|LayerID>19|BodyPartId>2|Id>2|Color>16762375;IsBodyPart>false|GoodID>8712|MediaResourceID>27527|GoodTypeID>4|LayerID>45|Id>8712;IsBodyPart>false|GoodID>9235|MediaResourceID>29235|GoodTypeID>94|LayerID>57|Id>9235"
    inv = ""
    # Текущая дата и время
    regdate = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S.0")
    bginv = ';339;349;430;431;'
    new_user = User(
        USERNAME=username,
        PASSWORD=hashed_password,
        ROLEFLAGS=2,
        LEVEL="999",
        AVATAR=ava,
        TICKET=new_ticket,
        INVENTORY=inv,
        REGDATE=regdate,
        BGInv=bginv
    )
    db.add(new_user)
    db.commit()
    return new_user.ID, None


def server_action_controller(db: Session, request: Request):
    query = db.query(User).filter_by(ID=request.session.get("userId")).first()
    if not query:
        sa_str = generate_server_action_xml_str(True)
        if not sa_str:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
    else:
        sa_str = generate_server_action_xml_str(False, request.session.get("userId"),
                                                request.session.get("ticket"), query.ROLEFLAGS, query.ISBANNED,
                                                query.USERNAME)

    return PlainTextResponse(content=sa_str, media_type="application/xml")


def add_gold_controller(db: Session, ticket: str, amount: int):
    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Обновляем значение GOLD
        user.GOLD += amount
        db.commit()
        return {"status_code": 200}
    else:
        raise HTTPException(status_code=404, detail="Пользователь не найден")


def add_money_controller(db: Session, ticket: str, amount: int):
    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Обновляем значение MONEY
        user.MONEY += amount
        db.commit()
        return
    else:
        raise HTTPException(status_code=404, detail="Пользователь не найден")


def ban_user_controller(db: Session, ticket: str):
    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user and user.ROLEFLAGS >= 131086:
        # Обновляем значение ISBANNED
        user.ISBANNED = 1
        db.commit()
        return
    else:
        return {"status_code": 403}


def update_bg_controller(db: Session, ticket: str, bg: str):
    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Обновляем значение BG
        user.BG = bg
        db.commit()
        return
    else:
        return {"status_code": 404}


def update_bg_inventory_controller(db: Session, ticket: str, inventory: str):
    # Ограничение на количество элементов в инвентаре фонов
    count = inventory.count(';')
    if count > 350:
        return {"error": "Inventory limit exceeded"}

    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Обновляем значение BGInv
        user.BGInv = inventory
        db.commit()
        return
    else:
        return {"status_code": 404}


def update_inventory_controller(db: Session, ticket: str, inventory: str):
    # Ограничение на количество элементов в инвентаре
    count = inventory.count('<ID>')
    if count > 240:
        return {"error": "Inventory limit exceeded"}

    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Обновляем значение INVENTORY
        user.INVENTORY = inventory
        db.commit()
        return
    else:
        return {"status_code": 404}


def update_money_controller(db: Session, ticket: str, priceRu: int, priceSm: int):
    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Обновляем значения GOLD и MONEY
        user.GOLD -= priceRu
        user.MONEY -= priceSm
        db.commit()
        return
    else:
        return {"status_code": 404}


def save_body_controller(db: Session, ticket: str, body_color: int, ears_color: int, ears: int, eyes: int, horns: int,
                         legs: int, legs_color: int, mouth: int, nose: int, peak: int):
    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Обновляем значения атрибутов тела
        user.BODY_COLOR = body_color
        user.EARS_COLOR = ears_color
        user.EARS = ears
        user.EYES = eyes
        user.HORNS = horns
        user.LEGS = legs
        user.LEGS_COLOR = legs_color
        user.MOUTH = mouth
        user.NOSE = nose
        user.PEAK = peak
        db.commit()
        return
    else:
        return {"status_code": 404}


def set_avatar_controller(db: Session, ticket: str, avatar: str):
    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Обновляем значение AVATAR
        user.AVATAR = avatar
        db.commit()
        return
    else:
        return {"status_code": 404}


def set_level_controller(db: Session, id: int, level: str):
    # Ищем пользователя по ID
    user = db.query(User).filter(User.ID == id).first()

    if user:
        # Обновляем значение LEVEL
        user.LEVEL = level
        db.commit()
        return level
    else:
        return {"status_code": 404}


def get_cabinet_json(db: Session, request: Request):
    user = db.query(User).filter(User.ID == request.session.get("userId")).first()
    if not user:
        return {"request": request}

    level = user.LEVEL
    # Преобразуем строку в объект даты и времени
    regdate = datetime.datetime.strptime(user.REGDATE.split('T')[0], "%Y-%m-%d")

    # Теперь можно использовать strftime
    regday = regdate.day
    regmonth = regdate.month
    regyear = regdate.year

    return {"request": request, "level": level, "regday": regday, "regmonth": regmonth, "regyear": regyear}


def cabinet_controller(db: Session, ticket: str, level: str, regday: int, regmonth: int, regyear: int):
    # Обновляем данные пользователя в базе данных
    user = db.query(User).filter(User.TICKET == ticket).first()
    if user:
        user.LEVEL = level
        # Обновляем REGDATE
        new_regdate = f"{regyear}-{regmonth:02d}-{regday:02d}T{user.REGDATE.split('T')[1]}"
        user.REGDATE = new_regdate
        db.commit()
        return "ОК, данные обновлены!"
    else:
        return ""
