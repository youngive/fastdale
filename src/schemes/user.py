from fastapi import Form
from pydantic import BaseModel, constr


class UserBase(BaseModel):
    USERNAME: constr(min_length=3, max_length=16, strict=True, pattern=r'^[\wа-яА-Я]+$')
    PASSWORD: constr(min_length=6, max_length=32, strict=True, pattern=r'^[\wа-яА-Я]+$')

    @classmethod
    def as_form(
            cls,
            USERNAME: constr(min_length=3, max_length=16, strict=True, pattern=r'^[\wа-яА-Я]+$') = Form(...),
            PASSWORD: constr(min_length=6, max_length=32, strict=True, pattern=r'^[\wа-яА-Я]+$') = Form(...)
    ):
        return cls(USERNAME=USERNAME, PASSWORD=PASSWORD)


class User(UserBase):
    ID: int
    AVATAR: str
    INVENTORY: str
    REGDATE: str
    LEVEL: str
    TICKET: str
    ROLEFLAGS: int
    BGInv: str
    HOUSE_STR: str
    ISBANNED: int = 0
    MONEY: int = 100
    GOLD: int = 0
    MAGIC: int = 0
    BG: str = '339'
    BODY_COLOR: int = 16762375
    LEGS: int = 55
    LEGS_COLOR: int = 16762375
    EARS: int = 98
    EARS_COLOR: int = 16762375
    EYES: int = 91
    NOSE: int = 68
    MOUTH: int = 67
    PEAK: int = 0
    HORNS: int = 0
    HOUSE_ID: int = 708

    class Config:
        from_attributes = True
