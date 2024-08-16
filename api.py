from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session


from sudoku import schemas as schema 

# change this back to the old model later
# from sudoku import schemas as sch
# sch.api.CommandIn
from sudoku.schemas.api import CommandIn, CommandOut
from sudoku.schemas.database import PuzBase, UserBase, User, UserCreate
from sudoku.schemas.keys import KeyBase
from sudoku.schemas.puzzle import SudokuOut

from sudoku.database import models
from sudoku.database.database import SessionLocal, engine
from sudoku.database.db_funcs import queries, update

from sudoku.classes.solver.Solver import Solver
from sudoku.classes.game.Board import Board

from sudoku.helper.helper import to_matrix

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# routes
@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

#response model/class doesnt seem to want to work
# will need to fix later
@app.post(
    '/test', response_model=CommandOut, status_code=200
)
async def test(payload: CommandIn):
    """tests CommandIn and CommandOut classes"""
    return CommandOut(
        com_return={ndx:i for ndx,i in enumerate(payload.commands)},
        com_in=payload # should set the input dictschema_keys. board
    )

@app.get(
    "/bt_predict/{puzzle}", 
    response_model=PuzBase,
    status_code=200
)
def get_prediction(commandsin: CommandIn):
    """Discord Command" `$h bt_predict 2d_sudoku_puzzle` """

    bad = [',','[',']']
    board = to_matrix(
        [int(i) for i in list(commandsin.commands[1]) 
         if i not in bad], n=9
        )

    solv = Solver(Board=None)
    solv.solve_sudoku(board)

    return PuzBase(
        puzzle=solv.pretty_rep(),
        difficulty=0
    ) 

@app.post(
    "/puzzle/",
    response_model=PuzBase
)
def get_puzzle(
    user: UserBase, 
    db: Session = Depends(get_db)
    ):
    """
    query database for user data

    user: UserBase schema
    db: database session

    returns Puzzle schema
    """
    return PuzBase(
        puzzle = queries.get_puzzle(db, user_id=user.id),
        difficulty=0 # need to add difficulties later
    )


@app.post(
    "/set_tile/{row}/{column}/{number}", 
    response_model=PuzBase
)
def set_tile(
    commandsin:CommandIn,
    row:int, column:int, number:int,
    db:Session=Depends(get_db)
    ):
    """
    update a users puzzle by a specific tile
    """
    # database functions should retrun the class
    return PuzBase(
        puzzle=update.update_puzzle_by_tile(
        db=db,
        user_id=commandsin.user_id,
        row=row,column=column,number=number
        ),
        difficulty=0 # a reminder to add difficulty later
    )

@app.get("/get_keys", response_model=PuzBase)
def get_keys(commandsin:CommandIn, db:Session=Depends(get_db)):
    """Get a full list of API keys"""
    return KeyBase(
        keys=queries.get_keys(db=db)
    )

@app.get("/get_keys/{user_id}")
def get_key(commandsin:CommandIn, db:Session=Depends(get_db)):
    return KeyBase(
        key=queries.get_key(
            db=db,
            user_id=commandsin.user_id
        )
    )


@app.post("/make_keys/{number}", response_model=CommandOut)
def create_user_keys(commandsin:CommandIn, number:int, db:Session=Depends(get_db)):
    """create user keys"""

    return CommandOut(
        com_return= {"key_status": True},
        com_in=commandsin
    )

# need to add a get user check to make sure you're not making copies
@app.post("/create_user", response_model=CommandOut)
def create_user(commandsin:CommandIn, db:Session=Depends(get_db)):
    """Create User"""

    user = update.create_user(
        db=db,
        user=UserCreate(
            username=commandsin.user,
            discord_id=commandsin.user_id,
            puzzle=''.join(['0' for i in range(81)]), # init with flat 0 string
        )
    )

    return CommandOut(
        com_return = {"user_created" : commandsin.user},
        com_in=commandsin
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port = 8000)



# [[9,1,3,0,0,0,5,0,0], 
# [6,0,7,0,0,0,0,2,4],
# [0,5,0,0,8,0,0,7,0],
# [0,7,9,0,0,0,0,0,0],
# [0,0,2,0,9,0,0,4,3],
# [0,0,0,0,0,4,0,9,0],
# [0,4,0,0,0,1,9,0,0],
# [7,0,6,0,0,9,0,0,5],
# [0,0,1,0,0,6,4,0,7]]
