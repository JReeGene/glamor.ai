from sqlalchemy.orm import Session

from api.schemas.user import UserCreate
from api.db.models.user import User
from api.core.hashing import Hasher 

def create_new_user(user: UserCreate, db:Session):
    user = User(
        email =user.email,
        password = Hasher.get_password_hash(user.password),
        is_active = True,
        is_superuser = False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user