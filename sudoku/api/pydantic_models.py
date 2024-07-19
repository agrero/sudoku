from pydantic import BaseModel


# use to and from dict
class SudokuIn(BaseModel):
    sudokuin: dict

class SudokuOut:
    sudokuout: dict
