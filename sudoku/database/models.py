from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    # name

    __tablename__ = "users"

    # components

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    discord_id = Column(Integer, unique=True, index=True)
    puzzle = Column(String(length=81))
    key = Column(Integer, unique=True)

    # user_puzzle = Column(String, ForeignKey("puzzles.puzzle"))
    # user_key = Column(String, unique=True)

    # relationships

    # rel_puzzle = relationship(
    #     "Puzzle", 
    #     foreign_keys=[user_puzzle]
    #     )


