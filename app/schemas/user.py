from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: Optional[int] = None
    username: str = Field(min_length=5, max_length=50)
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "Prueba",
                    "email": "prueba@gmail.com",
                    "password": "pass123",
                }
            ],
        }
    }