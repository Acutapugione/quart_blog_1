from quart import redirect, url_for
from . import app
from .post import posts


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for(posts.__name__))
