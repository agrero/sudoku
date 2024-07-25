from sudoku.classes.game.Board import Board

from fastapi.encoders import jsonable_encoder

# might stand to benefit to convert
#  each row into a string for just pure legibility
examples_SudokuIn = [{
    "normal": {
        "board": jsonable_encoder(Board()), 
        "model" : "model name",
        "search" : True
    }
}]

examples_SudokuOut = [{
    "normal": {
        "board": jsonable_encoder(Board()), 
        "valid" : True,
        "sudokuin" : {
            "board": jsonable_encoder(Board()), 
            "model" : "model name",
            "search" : True
        }
    }
}]
