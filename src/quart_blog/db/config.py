from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from . import AutoTableNameMixin, AutoPrimaryKeyMixin


class Base(
    DeclarativeBase,
    AutoTableNameMixin,
    AutoPrimaryKeyMixin,
):
    """docstring for Base."""


class Config(object):
    """docstring for Config."""

    BASE = Base
    ENGINE = create_engine("sqlite:///blog.db", echo=True)
    SESSION = sessionmaker(ENGINE)

    @classmethod
    def up(cls):
        cls.BASE.metadata.create_all(cls.ENGINE)

    @classmethod
    def down(cls):
        cls.BASE.metadata.drop_all(cls.ENGINE)
