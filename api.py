from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder

from sudoku.classes.solver.Solver import Solver
from sudoku.helper.helper import to_matrix

from sqlalchemy.orm import Session


from sudoku.database.db_funcs import queries, update

from sudoku.database import models
from sudoku.database.database import SessionLocal, engine

from sudoku import schemas

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
    '/test', response_model=schemas.api.CommandOut, status_code=200
)
async def test(payload: schemas.api.CommandIn):
    """tests CommandIn and CommandOut classes"""
    return schemas.api.CommandOut(
        com_return={ndx:i for ndx,i in enumerate(payload.commands)},
        com_in=payload # should set the input dict to kwargs
    )

@app.post("/bt_predict", response_model=schemas.sudoku.SudokuOut,status_code=200)
def get_prediction(commandsin: schemas.api.CommandIn):
    """Discord Command" `$h bt_predict 2d_sudoku_puzzle` """

    bad = [',','[',']']
    board = to_matrix(
        [int(i) for i in list(commandsin.commands[1]) if i not in bad], 9
        )

    solv = Solver(Board=None)
    solv.solve_sudoku(board)

    return schemas.sudoku.SudokuOut(
        solved_board=solv.board,
        valid=sum(solv.flatten_board()) == 405, # if solved should equal 405,
        commandsin=jsonable_encoder(commandsin)
    )



@app.post("/puzzle/", response_model=schemas.database.PuzBase)
def get_puzzle(
    user: schemas.database.UserBase, 
    db: Session = Depends(get_db)
    ):
    """
    query database for user data

    user: UserBase schema
    db: database session

    returns Puzzle schema
    """
    return schemas.database.Puz(
        puzzle = get_puzzle(db, user_id=user.id),
        difficulty=0 # need to add difficulties later
    )


@app.post("/puzzle/set_tile/{row}/{column}/{number}", response_model=schemas.database.PuzBase)
def set_tile(
    commandsin:schemas.api.Commandsin,
    row, column, number,
    db:Session=Depends(get_db)
    ):
    """
    update a users puzzle by a specific tile
    """

    puzzle = update.update_puzzle_by_tile(
        db=db,
        user_id=commandsin.user_id,
        row=row, column=column, number=number
    )

    return schemas.database.PuzBase(
        puzzle=puzzle,
        difficulty=0 # a reminder to add difficulty later
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
