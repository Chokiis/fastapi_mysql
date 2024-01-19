from models.admin import Admin as AdminModel
from schemas.admin import Admin

class AdminService():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_admin(self, id):
        result = self.db.query(AdminModel).filter(AdminModel.id == id).first()
        return result