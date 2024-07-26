from fastapi import FastAPI

from sudoku.pydantic.models import *
from sudoku.classes.solver.Solver import Solver
from sudoku.helper.helper import to_matrix

from sudoku.pydantic.models import CommandIn, CommandOut

app = FastAPI()

# routes
@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


#response model/class doesnt seem to want to work
# will need to fix later
@app.post('/test', response_model=CommandOut, status_code=200)
async def test(payload: CommandIn):

    return CommandOut(
        com_return={ndx:i for ndx,i in enumerate(payload.commands)},
        com_in=payload # should set the input dict to kwargs
    )

@app.post("/bt_predict", response_model=SudokuOut,status_code=200)
def get_prediction(commandsin: CommandIn):
    """Discord Command" `$h bt_predict 2d_sudoku_puzzle` """

    bad = [',','[',']']
    board = to_matrix(
        [int(i) for i in list(commandsin.commands[1]) if i not in bad], 9
        )

    solv = Solver(Board=None)
    solv.solve_sudoku(board)

    return SudokuOut(
        solved_board=solv.board,
        valid=sum(solv.flatten_board()) == 405, # if solved should equal 405,
        commandsin=jsonable_encoder(commandsin)
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
