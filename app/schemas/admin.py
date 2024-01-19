from typing import Optional
from pydantic import BaseModel, Field

class Admin(BaseModel):
    id: Optional[int] = None
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "prueba@gmail.com",
                    "password": "pass123",
                }
            ],
        }
    }