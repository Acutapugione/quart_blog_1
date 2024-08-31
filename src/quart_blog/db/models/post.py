from typing import List
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func
from . import Config


class Post(Config.BASE):
    title: Mapped[str]
    content: Mapped[str]
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    author: Mapped["Author"] = relationship(back_populates="posts")
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
