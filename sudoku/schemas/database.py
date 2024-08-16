from pydantic import BaseModel


class PuzBase(BaseModel):
    puzzle: str
    difficulty: int | None = None

class PuzCreate(PuzBase):
    pass

class Puz(PuzBase):
    owner_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    discord_id: int

class User(UserBase):
    puzzle: str 

    class Config:
        from_attributes = True

class UserCreate(User):
    pass