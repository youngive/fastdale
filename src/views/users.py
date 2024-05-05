from sqlalchemy.orm import Session

from src.models.user import User


def get_user_data_view(db: Session, ticket: str):
    # Ищем пользователя по TICKET
    user = db.query(User).filter(User.TICKET == ticket).first()

    if user:
        # Формируем строку с данными пользователя
        user_data = (
            "id={}&username={}&level={}&regdate={}&roleflags={}&money={}&gold={}&magic={}&avatar={}&inventory={}&isbanned={}&bg={}&bginven={}&body_color={}&legs={}&legs_color={}&ears={}&ears_color={}&eyes={}&nose={}&mouth={}&peak={}&horns={}&house_id={}&house_str={}".format(
                user.ID,
                user.USERNAME,
                user.LEVEL,
                user.REGDATE,
                user.ROLEFLAGS,
                user.MONEY,
                user.GOLD,
                user.MAGIC,
                user.AVATAR,
                user.INVENTORY,
                user.ISBANNED,
                user.BG,
                user.BGInv,
                user.BODY_COLOR,
                user.LEGS,
                user.LEGS_COLOR,
                user.EARS,
                user.EARS_COLOR,
                user.EYES,
                user.NOSE,
                user.MOUTH,
                user.PEAK,
                user.HORNS,
                user.HOUSE_ID,
                user.HOUSE_STR
            )
        )
        return user_data
    else:
        # Если пользователь не найден, возвращаем пустую строку
        return ""
