from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


print("hello")

app = FastAPI()


@app.get("/")  # decorator , fastapi instance, http method, path
def read_root():  # path operation function , function name doesn't matter
    return {"Hello": "World -"}


@app.get("/posts")
def get_posts():
    return {"posts": ["apple", "tesla"]}


# title : str, content : str
@app.post("/createpost")
def create_post(payload: dict = Body(...)):  # take body, convert to a dict,
    print(payload)
    return {"status": f'success , title= {payload["title"]}'}


# title : str, content : str
@app.post("/createpost2")
def create_post(post: Post):  #  convert to pandantic Post model
    d = post.dict()  # convert pandantic model to dict
    print(post.title)
    return {
        "status": f"success , title= { post.title} , published = {post.published} , content = {d['content']}"
    }
