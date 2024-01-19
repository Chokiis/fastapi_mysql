from models.user import User as UserModel
from schemas.user import User

class UserService():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_users(self):
        result = self.db.query(UserModel).all()
        return result
    
    def create_user(self, user: User):
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
    
    def get_user(self, id): 
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result
    
    def user_update(self, id: int, data: User):
        user_up = self.db.query(UserModel).filter(UserModel.id == id).first()
        user_up.username = data.username
        user_up.email = data.email
        user_up.password = data.password
        self.db.commit()
        return
    def user_delete(self, id: int):
        user_del = self.get_user(id)
        self.db.delete(user_del)
        self.db.commit()
        return