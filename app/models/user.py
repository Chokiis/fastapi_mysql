from config.database import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class User(Base):
    __tablename__ = "users"
    
    id = Column(INTEGER,primary_key=True)
    username = Column(VARCHAR(50))
    email = Column(VARCHAR(50))
    password = Column(VARCHAR(50))
