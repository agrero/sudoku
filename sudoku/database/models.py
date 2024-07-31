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
    prev_puzzle = Column(String, ForeignKey("puzzles.puzzle"))
    key = Column(String, ForeignKey("keys.key"))

    # relationships

    puzzle = relationship("Puzzle", back_populates="owner_id")
    key = relationship("Keys", back_populates="key")

class Puzzle(Base):
    # name

    __tablename__ = "puzzles"

    # components

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), unique=True)
    puzzle = Column(String, index=True)

    # relationships

    owner = relationship("User", back_populates="puzzle")

class Keys(Base):
    """
    Table Name: keys

    # components
    id: Column of integers *primary keys*
    owner_id: Column of integers as derove from owner_id 
        from the users table
    key: Column of api keys as strings
    """
    # name

    __tablename__ = "keys"

    # components

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.username"), unique=True)
    key = Column(String)

    # relationships

    owner = relationship("User", back_populates="owner_id")