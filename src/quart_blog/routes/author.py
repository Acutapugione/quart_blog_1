from sqlalchemy import select
from . import Author, app, Config


@app.get("/authors")
async def authors():
    with Config.SESSION.begin() as session:
        smth = select(Author)
        authors = session.scalars(smth).all()
        return authors
