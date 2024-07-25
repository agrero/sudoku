from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sudoku.api.pydantic.models import *
from sudoku.classes.solver.Solver import Solver

from  import CommandIn
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
