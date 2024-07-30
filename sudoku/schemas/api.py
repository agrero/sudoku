from pydantic import BaseModel
from sudoku.schemas.forms.examples import *


class CommandIn(BaseModel):
    # theoretically we could make our own allowed string class
    # to make commands: list[AllowedStr]
    commands: list[str] 
    user: str
    user_id: int
    message_id: int
    guild_id: int

class CommandOut(BaseModel):
    com_return: dict
    com_in: CommandIn | None = None # return the commands input

