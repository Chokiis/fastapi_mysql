from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from config.database import Base

class Admin(Base):
    __tablename__ = "admins"
    
    id = Column(INTEGER, primary_key=True)
    email = Column(VARCHAR(50))
    password = Column(VARCHAR(50))