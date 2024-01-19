from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from services.user import UserService
from schemas.user import User
from config.dependencies import get_db
from middleware.jwt_bearer import JWTBearer

user_router = APIRouter()

# CONSULTA AL TABLA 'user'
@user_router.get('/users/', tags = ['Users'], response_model=List[User], status_code=200, dependencies=[Depends(JWTBearer())])
async def get_users(db: Session = Depends(get_db))-> List[User]:
    result = UserService(db).get_users()
    return result

@user_router.get('/users/{id}', tags=['Users'], status_code=200, response_model=User, dependencies=[Depends(JWTBearer())])
async def get_user(id: int = Path(ge=1, le=2000), db: Session = Depends(get_db)):
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return result

@user_router.post('/users/', tags=['Users'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
async def create_user(user: User, db: Session = Depends(get_db))-> dict:
    UserService(db).create_user(user)
    return JSONResponse(content={"Message": "Se ha registrado un nuevo usuario"})

@user_router.put('/users/', tags=['Users'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
async def user_update(id: int, user: User, db: Session = Depends(get_db)):
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
    UserService(db).user_update(id, user)
    return JSONResponse(status_code=200, content={"message": "Usuario actualizado"})

@user_router.delete('/users/{id}', tags=["Users"], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
async def user_delete(id: int, db: Session = Depends(get_db)):
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
    UserService(db).user_delete(id)
    return JSONResponse(status_code=200, content={"message": "Usuario eliminado con éxito"})
