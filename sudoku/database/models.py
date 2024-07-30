from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    # name

    __tablename__ = "users"

    # componenents

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    discord_id = Column(Integer, unique=True, index=True)
    prev_puzzle = Column(String, ForeignKey("puzzle.puzzle"))

    # relationships

    puzzle = relationship("Puzzle", back_populates="owner")

class Puzzle(Base):
    # name

    __tablename__ = "puzzle"

    # components

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), unique=True)
    puzzle = Column(String, index=True)

    # relationships

    owner = relationship("User", back_populates="puzzle")
