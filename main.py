from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles

from src.routers.external.asynch.Ping import router as ping_router
from src.routers.external.asynch.ServerAction import router as server_action_router
from src.routers.external.pages import router as pages_router
from src.routers.internal.api.addGold import router as add_gold_router
from src.routers.internal.api.addMoney import router as add_money_router
from src.routers.internal.api.ban import router as ban_router
from src.routers.internal.api.bg import router as bg_router
from src.routers.internal.api.bginv import router as bg_inv_router
from src.routers.internal.api.inv import router as inv_router
from src.routers.internal.api.kek import router as kek_router
from src.routers.internal.api.money import router as money_router
from src.routers.internal.api.saveBody import router as save_body_router
from src.routers.internal.api.setAvatar import router as set_avatar_router
from src.routers.internal.api.setLevel import router as set_level_router
from src.routers.external.api.cabinet import router as cabinet_router

from src.utilities.const import Const as cst
import src.utilities.config as cfg
from src.utilities.logger import CustomLogger
from src.utilities.network import check_for_updates

# from src.models.database import engine
# from src.models import user

# user.Base.metadata.create_all(bind=engine)

app = FastAPI(
    debug=True,
    title="FastDale"
)

app.include_router(router=pages_router)

app.include_router(router=ping_router)
app.include_router(router=server_action_router)
app.include_router(router=pages_router)
app.include_router(router=add_gold_router)
app.include_router(router=add_money_router)
app.include_router(router=ban_router)
app.include_router(router=bg_router)
app.include_router(router=bg_inv_router)
app.include_router(router=inv_router)
app.include_router(router=kek_router)
app.include_router(router=money_router)
app.include_router(router=save_body_router)
app.include_router(router=set_avatar_router)
app.include_router(router=set_level_router)

app.include_router(router=cabinet_router)

if cfg.minfs:
    from src.routers.external.fs import router as fs_router

    app.include_router(router=fs_router)
app.mount("/", StaticFiles(directory="assets/static"))

# SessionMiddleware с секретным ключом
app.add_middleware(SessionMiddleware, secret_key=cfg.secretkey)

logger = CustomLogger()

if cfg.checkforupdates:
    link = check_for_updates(cst.CURRENT_VERSION)
    if link:
        print(logger.log(f"Доступно обновление fastdale по ссылке: {link}"))
    else:
        print(logger.log(f"Ты пользуешься последней версией {cst.CURRENT_VERSION}"))
