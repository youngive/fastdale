from sqlalchemy import Column, Integer, String

from .database import Base

class User(Base):
    __tablename__ = "users"

    ID = Column(Integer, primary_key=True, index=True)
    USERNAME = Column(String(255), nullable=False)
    PASSWORD = Column(String(255), nullable=False)
    AVATAR = Column(String(10000), nullable=False)
    INVENTORY = Column(String(10000), nullable=False)
    REGDATE = Column(String(255), nullable=False)
    LEVEL = Column(String(255), nullable=False)
    TICKET = Column(String(255), nullable=False)
    ROLEFLAGS = Column(Integer, nullable=False)
    ISBANNED = Column(Integer, nullable=False, default=0)
    MONEY = Column(Integer, nullable=False, default=100)
    GOLD = Column(Integer, nullable=False, default=0)
    MAGIC = Column(Integer, nullable=False, default=0)
    BG = Column(String(255), nullable=False, default='339')
    BGInv = Column(String(10000), nullable=False)
    BODY_COLOR = Column(Integer, nullable=False, default=16762375)
    LEGS = Column(Integer, nullable=False, default=55)
    LEGS_COLOR = Column(Integer, nullable=False, default=16762375)
    EARS = Column(Integer, nullable=False, default=98)
    EARS_COLOR = Column(Integer, nullable=False, default=16762375)
    EYES = Column(Integer, nullable=False, default=91)
    NOSE = Column(Integer, nullable=False, default=68)
    MOUTH = Column(Integer, nullable=False, default=67)
    PEAK = Column(Integer, nullable=False, default=0)
    HORNS = Column(Integer, nullable=False, default=0)
    HOUSE_ID = Column(Integer, nullable=False, default=708)
    HOUSE_STR = Column(String(10000), nullable=False)