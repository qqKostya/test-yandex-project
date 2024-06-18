from fastapi import FastAPI
from . import database, crud, schemas


app = FastAPI()

# Dependency injection for database session
database.Base.metadata.create_all(bind=database.engine)


@app.post("/users/")
def create_user(user: schemas.UserCreate):
    return crud.create_user(db_session=database.SessionLocal(), user=user)


@app.get("/users/")
def read_users():
    return crud.get_users(db_session=database.SessionLocal())
