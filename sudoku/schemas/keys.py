from pydantic import BaseModel

class KeyBase(BaseModel):
    key: str | None
    keys: list[str] | None
