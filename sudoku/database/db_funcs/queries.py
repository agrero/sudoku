from sqlalchemy.orm import Session

from .. import models

# seperating these based on queries/deletions/updates may be nice later
# change *get* in these to *query*


def get_user(db: Session, user_id: int):
    return db.query(
        models.User
    ).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(
        models.User
    ).offset(skip).limit(limit).all()

def get_puzzle(db: Session, user_id: int):
    """
    get a users puzzle from a database

    db: database Session
    user_id: integer, should be inputted as an attribute
        of a pydantic model

    returns: database query of Puz schema
    """

    return db.query(
        models.Puzzle # query puzzle model
    ).filter(models.Puzzle.owner_id == user_id).first() # ids match

def get_puzzles(db: Session, skip: int = 0, limit: int = 100):
    """query puzzle database for all puzzles"""
    return db.query(
        models.Puzzle
    ).offset(skip).limit(limit).all()

def get_keys(db: Session, skip: int = 0, limit:int = 100):
    return db.query(
        models.Keys
    ).offset(skip).limit(limit).all()

def get_key(db: Session, user_id: int):
    return db.query(
        models.Keys
    ).filter(models.Keys.owner_id == user_id).first()
