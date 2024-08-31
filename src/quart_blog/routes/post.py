from sqlalchemy import select
from quart import render_template, request, redirect, url_for
from . import Author, Post, app, Config

# from . import Author, app, Config


@app.post("/posts")
async def create_post():
    form = await request.form
    if form:
        with Config.SESSION.begin() as session:
            post = Post(
                **form,
                author=Author(name="acuta"),
            )
            session.add(post)
    return redirect(url_for("posts"))


@app.get("/post_details/<int:index>", defaults={"index": 0})
async def post_details(index: int): ...


@app.get("/posts")
async def posts():
    with Config.SESSION.begin() as session:
        smth = select(Post)
        posts = session.scalars(smth).all()
        return await render_template(
            "index.html",
            posts=[
                Post(
                    created=x.created,
                    content=x.content,
                    author=x.author,
                    title=x.title,
                )
                for x in posts
            ],
        )
