from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import src.utilities.config as cfg
# Указываете строку подключения к вашей MySQL базе данных
# Формат строки асинхронного подключения для MySQL: "mariadb+aiomysql://<username>:<password>@<host>/<dbname>"
SQLALCHEMY_DATABASE_URL = f"mariadb+pymysql://{cfg.dbuser}:{cfg.dbpassword}@{cfg.dbhost}/{cfg.dbname}"

# Создаем движок SQLAlchemy для работы с MySQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создаем сессию для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
