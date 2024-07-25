from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sudoku.api.pydantic.models import *
from sudoku.classes.solver.Solver import Solver

from sudoku.api.pydantic.models import CommandIn

app = FastAPI()

# routes
@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


#response model/class doesnt seem to want to work
# will need to fix later
@app.post('/test', status_code=200)
async def test(payload: CommandIn):

    return payload.commands

@app.post("/bt_predict", status_code=200)
def get_prediction(payload: SudokuIn):

    solv = Solver(Board=None)
    solv.board = solv.from_dict(
        payload.sudokuin
        )
    solv.solve_sudoku(solv.board)
    
    out = SudokuOut()
    out.sudokuout = solv.to_dict()

    return out

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port = 8000)
