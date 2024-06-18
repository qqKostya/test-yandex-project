from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db_session: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        password_hash=user.password_hash,
        email=user.email
    )
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user


def get_users(db_session: Session):
    return db_session.query(models.User).all()
