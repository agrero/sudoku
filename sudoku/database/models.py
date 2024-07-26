from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    prev_puzzle = Column(String, ForeignKey("puzzle.puzzle"))

    puzzle = relationship("Puzzle", back_populates="owner")

class Puzzle(Base):
    __tablename__ = "puzzle"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), unique=True)
    puzzle = Column(String, index=True)

    owner = relationship("User", back_populates="puzzle")
