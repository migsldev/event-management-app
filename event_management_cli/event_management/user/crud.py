# event_management/user/crud.py

from sqlalchemy.orm import Session
from .models import User

# Create a User
def create_user(db: Session, username: str, password: str):
    db_user = User(username=username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all Users
def get_users(db: Session):
    return db.query(User).all()

# Get a User by Username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Get a User by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Delete a User
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
