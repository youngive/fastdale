from fastapi import Form
from pydantic import BaseModel, conint, Field


class BaseRequest(BaseModel):
    ticket: str


class CurrencyRequest(BaseRequest):
    amount: int

    @classmethod
    def as_form(
            cls,
            ticket: str = Form(...),
            amount: int = Form(...)
    ):
        return cls(ticket=ticket, amount=amount)


class BanRequest(BaseRequest):
    user_id: int

    @classmethod
    def as_form(
            cls,
            ticket: str = Form(...),
            user_id: int = Form(...)
    ):
        return cls(ticket=ticket, user_id=user_id)


class BgRequest(BaseRequest):
    bg: str

    @classmethod
    def as_form(
            cls,
            ticket: str = Form(...),
            bg: str = Form(...)
    ):
        return cls(ticket=ticket, bg=bg)


class BgInvRequest(BaseRequest):
    inventory: str

    @classmethod
    def as_form(
            cls,
            ticket: str = Form(...),
            inventory: str = Form(...)
    ):
        return cls(ticket=ticket, inventory=inventory)


class InvRequest(BaseRequest):
    inventory: str

    @classmethod
    def as_form(
            cls,
            ticket: str = Form(...),
            inventory: str = Form(...)
    ):
        return cls(ticket=ticket, inventory=inventory)


class MoneyRequest(BaseRequest):
    priceRu: int
    priceSm: int

    @classmethod
    def as_form(
            cls,
            ticket: str = Form(...),
            priceRu: int = Form(...),
            priceSm: int = Form(...)
    ):
        return cls(ticket=ticket, priceRu=priceRu, priceSm=priceSm)


class BodyRequest(BaseRequest):
    body_color: int
    ears_color: int
    ears: int
    eyes: int
    horns: int
    legs: int
    legs_color: int
    mouth: int
    nose: int
    peak: int

    @classmethod
    def as_form(
            cls,
            ticket: str = Form(...),
            body_color: int = Form(...),
            ears_color: int = Form(...),
            ears: int = Form(...),
            eyes: int = Form(...),
            horns: int = Form(...),
            legs: int = Form(...),
            legs_color: int = Form(...),
            mouth: int = Form(...),
            nose: int = Form(...),
            peak: int = Form(...)
    ):
        return cls(ticket=ticket, body_color=body_color, ears_color=ears_color, ears=ears, eyes=eyes, horns=horns,
                   legs=legs, legs_color=legs_color, mouth=mouth, nose=nose, peak=peak)


class AvaRequest(BaseRequest):
    avatar: str

    @classmethod
    def as_form(
            cls,
            ticket: str = Form(...),
            avatar: str = Form(...)
    ):
        return cls(ticket=ticket, avatar=avatar)


class LvlRequest(BaseModel):
    id: int
    level: str = Field(..., max_length=5)

    @classmethod
    def as_form(
            cls,
            id: int = Form(...),
            level: str = Form(...)
    ):
        return cls(id=id, level=level)


class CabinetRequest(BaseModel):
    level: str = Field(..., max_length=5)
    regday: conint(ge=1, le=31)
    regmonth: conint(ge=1, le=12)
    regyear: conint(ge=1000, le=2100)

    @classmethod
    def as_form(
            cls,
            level: str = Form(...),
            regday: int = Form(...),
            regmonth: int = Form(...),
            regyear: int = Form(...)
    ):
        return cls(level=level, regday=regday, regmonth=regmonth, regyear=regyear)
