from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.admin import Admin
from config.database import Session
from config.dependencies import get_db
from services.admin import AdminService

admin_router = APIRouter()

@admin_router.post('/admin/{id}', tags=['Auth'])
def login(admin: Admin, db: Session = Depends(get_db), id: int = Path(ge=1, le=2000)):
    result = AdminService(db).get_admin(id)
    if id == result.id and admin.password == result.password:
        token: str = create_token(admin.model_dump())
        return token