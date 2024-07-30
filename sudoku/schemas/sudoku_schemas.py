from pydantic import BaseModel
from sudoku.schemas.forms.examples import *
from ..schemas.api_schemas import CommandIn

class SudokuIn(BaseModel):
    """Sudoku Input Model
    board: json-encoded Board class \
    model: prediction model 
        choices are: ['backtrack','CNN'] \
    search: whether or not you want to parse 
        the database for if this was previously 
        answered \
        """
    board: dict # board object dump
    model: str | None # if we change this to list we can do multiple preds at a time
    search: bool | None 
    
    # standardize later
    model_config = {
        "json_schema_extra": {
            "examples": examples_SudokuIn
        }
    }

class SudokuOut(BaseModel):
    """
    Sudoku Output Model

    board: json-encoded Board class
    valid: the solvability of the Sudoku Puzzle
    sudokuin: pydantic SudokuIn class, typically
        just returning the initial input
    """
    solved_board: list # board object dump
    valid: bool
    commandsin: CommandIn

    # standardize later
    model_config = {
        "json_schema_extra": {
            "examples": examples_SudokuOut
        }
    }
