from quart import Quart
from .db import Config


app = Quart(__name__)

from . import routes


def run() -> None:
    try:
        Config.up()
        app.run()

    except Exception as e:
        raise e
    finally:
        Config.down()
