from sqlalchemy.orm import Session

from .. import models



def get_user(db: Session, user_id: int) -> Session.query:
    """
    get singular user through a given user_id

    db: database Session
    user_id: integer of a given user's id

    returns: datababase query of the given user
    """
    return db.query(
        models.User
    ).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> Session.query:
    """
    get singular user through a given user_id

    db: database Session
    user_id: integer of a given user's id

    returns: datababase query of the given user
    """
    return db.query(
        models.User
    ).offset(skip).limit(limit).all()

def get_puzzle(db: Session, user_id: int) -> Session.query:
    """
    get a users puzzle from a database

    db: database Session
    user_id: integer of a given user's id

    returns: database query of Puz schema
    """

    return db.query(
        models.Puzzle # query puzzle model
    ).filter(models.Puzzle.owner_id == user_id).first() # ids match

def get_puzzles(db: Session, skip: int = 0, limit: int = 100) -> Session.query:
    """
    query for all puzzles

    db: database Session
    skip: number of initial values to skip
    limit: maximum number of values to return

    returns session query of all puzzles
    """
    return db.query(
        models.Puzzle
    ).offset(skip).limit(limit).all()

def get_keys(db: Session, skip: int = 0, limit:int = 100) -> Session.query:
    """
    query for all keys 

    db: database Session
    skip: number of initial values to skip
    limit: maximum number of values to return

    returns session query of all keys
    """
    return db.query(
        models.Keys
    ).offset(skip).limit(limit).all()

def get_key(db: Session, user_id: int) -> Session.query:
    """
    query for a given users key 

    db: database Session
    user_id : integer representation of a user ID
    
    returns session query of all keys
    """
    return db.query(
        models.Keys
    ).filter(models.Keys.owner_id == user_id).first()
