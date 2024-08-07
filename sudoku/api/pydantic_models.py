from pydantic import BaseModel

from typing import Optional


# use to and from dict
class SudokuIn(BaseModel):
    sudokuin: dict
    model: Optional[str]
    search: Optional[bool]

class SudokuOut:
    sudokuout: dict
    model: Optional[str]
    completed: bool
