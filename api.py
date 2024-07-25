from fastapi import FastAPI

from sudoku.pydantic.models import *
from sudoku.classes.solver.Solver import Solver

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
def get_prediction(sudoku: SudokuIn):

    solv = Solver(Board=None)
    solv.solve_sudoku(sudoku.board)

    return SudokuOut(
        board=solv.board,
        valid=sum(solv.flatten_board()) == 405, # if solved should equal 405,
        sudokuin=sudoku
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port = 8000)
