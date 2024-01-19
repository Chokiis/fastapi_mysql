# main.py
from fastapi import FastAPI
from config.database import engine, Base
from config.connection import dbConnection
from routers.user import user_router
from routers.admin import admin_router
from contextlib import asynccontextmanager

app = FastAPI()
app.title = "VINOC"
app.version = "0.0.1"

# Conexión a db
@asynccontextmanager
async def lifespan():
    dbConnection()
    yield

# Crea la base de datos
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(admin_router)
app.include_router(user_router)

# @app.on_event("startup")
# async def start_auth_admin():
#     client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URL)
#     await init_beanie(
#         database=client[config.bdConnect], document_models=_auth_models_
#     )
    
#     app.include_router(
#         auth, 
#         prefix="/auth",
#         tags=["Admin - Authentication"],
#         )
#     contact_client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URL)

# Resto del código FastAPI...
# @app.get('/', tags=['Home'])
# def message():
#     return "Hola mundo"

