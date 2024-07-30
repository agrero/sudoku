from pydantic import BaseModel


class PuzBase(BaseModel):
    puzzle: str
    difficulty: int | None = None

class PuzCreate(PuzBase):
    pass

class Puz(PuzBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    discord_id: int

class User(UserBase):
    id: int
    is_active: bool
    puzzle: str 

    class Config:
        from_attributes = True