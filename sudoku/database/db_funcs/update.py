from sqlalchemy.orm import Session

from sudoku.database.db_funcs import queries

from sudoku import schemas

from sudoku import schemas

from .. import models

# technically create not update
def create_user(db: Session, user: schemas.database.UserCreate):
    db_user = models.User(
        username = user.username,
        discord_id = user.discord_id,
        puzzle = user.puzzle 
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # in the future change this so it doesn't 
    # return a database object but the 
    # usercreate parameters
    return db_user

# technically create not update
def create_user_puzzles(
        db: Session, puzzle: schemas.database.PuzCreate, user_id: int
        ):
    """
    create a user puzzle in a database

    db: database Sesssion as defined in SessionLocal in database.py controller
    puzzle: a sudoku puzzle contained within a PuzCreate wrapper shema
    user_id: a given user id to give this new puzzle to
        - in practice this should come from a User schema
    """
    # create item in db schema by dumping pydantic model
    db_puz = models.Puzzle(**puzzle.model_dump(), owner_id=user_id)

    # add and refresh to database

    # I think if we make this the init method of a Session wrapper class
    # that might work as an alternative here
    db.add(db_puz)
    db.commit()
    db.refresh(db_puz)
    
    # return item
    return db_puz # use this for testing!

def update_puzzle_by_tile(
        db: Session, user_id: int, row:int, column:int, number:int
    ):
    """updates a given users puzzle
    
    returns: Puzzle schema"""
    
    # get puzzle
    puzzle = list(
        queries.get_puzzle(db = Session, user_id=user_id).puzzle
        )
    puzzle[row][column] = number

    # update puzzle
    db.add(puzzle)
    db.commit()
    db.refresh(puzzle)

    return puzzle

