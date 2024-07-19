from fastapi import FastAPI, HTTPException

from sudoku.api.pydantic_models import *
from sudoku.classes.solver.Solver import Solver

import json

app = FastAPI()

# routes

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

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

    uvicorn.run(app, host='0.0.0.0', port = 8008, workers=1)
