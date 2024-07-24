from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sudoku.api.pydantic_models import *
from sudoku.classes.solver.Solver import Solver

import json

# I think this should go like 
# method 1: acts as a wrapper for method 2
# /predict

# method 2: does the actual prediction
# -> /predict/{model}

app = FastAPI()

# routes

origins = [
    'http://localhost:3000',
    'localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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

    uvicorn.run(app, port = 8000)
