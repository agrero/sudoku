from pydantic import BaseModel
from sudoku.pydantic.forms.examples import *



class SudokuIn(BaseModel):
    board: dict # board object dump
    model: str | None
    search: bool | None 
    # standardize later
    model_config = {
        "json_schema_extra": {
            "examples": examples_SudokuIn
        }
    }

class SudokuOut(BaseModel):
    board: dict # board object dump
    valid: bool
    sudokuin: SudokuIn

    # standardize later
    model_config = {
        "json_schema_extra": {
            "examples": examples_SudokuOut
        }
    }

class CommandIn(BaseModel):
    commands: list[str] 
    user: str
    message_id: int
    guild_id: int

class CommandOut(BaseModel):
    com_return: dict
    com_in: CommandIn | None = None # return the commands input

