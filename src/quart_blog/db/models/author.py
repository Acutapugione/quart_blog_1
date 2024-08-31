from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Config


class Author(Config.BASE):
    name: Mapped[str]

    posts: Mapped[List["Post"]] = relationship(back_populates="author")
