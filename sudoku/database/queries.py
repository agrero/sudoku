from sqlalchemy.orm import Session
from sqlalchemy import update

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username = user.username,
        discord_id = user.discord_id 
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_puzzle(db: Session, user_id: int):
    return db.query(
        models.User
    ).filter(models.User.id == user_id).first()

def update_puzzle(db: Session, user_id:int, puzzle:str):
    stmt = (
        update(models.User)                 # Update database 
        .where(models.User.id == user_id)   # where the userid matches the query
        .values(prev_puzzle = puzzle)       # update puzzle with new value
    )
    return db.execute(stmt)

def get_puzzles(db: Session, skip: int = 0, limit: int= 100):
    return db.query(models.Puzzle).offset(skip).limit(limit).all()

def create_user_puzzles(db: Session, puzzle: schemas.PuzCreate, user_id: int):
    """
    create a user puzzle in a database

    db: database Sesssion as defined in SessionLocal in database.py controller
    puzzle: a sudoku puzzle contained within a PuzCreate wrapper shema
    user_id: a given user id to give this new puzzle to
        - in practice this should come from a User schema
    """
    # create item in db schema by dumping pydantic model
    db_puz = models.Item(**puzzle.model_dump(), owner_id=user_id)

    # add and refresh to database
    db.add(db_puz)
    db.commit()
    db.refresh(db_puz)
    
    # return item
    return db_puz # use this for testing!