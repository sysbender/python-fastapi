from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from random import randrange
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "fruit", "content": "apple, orange, banana", "id": 1},
    {"title": "vegetable", "content": "reddit, tomato , potato", "id": 2},
]


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
    return None


app = FastAPI()


@app.get("/")  # decorator , fastapi instance, http method, path
def read_root():  # path operation function , function name doesn't matter
    return {"Hello": "World -"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/posts/{id}")  # id - path parameter
def get_post(id: int):  # convert to int and validate by fastapi
    print(f"get post by id= {id}")

    post = find_post(id)

    return {"data": post}


# title : str, content : str
@app.post("/v1/posts")
def create_post(payload: dict = Body(...)):  # take body, convert to a dict,
    print(payload)
    return {"status": f'success , title= {payload["title"]}'}


# title : str, content : str
@app.post("/posts")
def create_post(post: Post):  #  convert to pandantic Post model
    post_dict = post.dict()  # convert pandantic model to dict
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)

    return {"data": post_dict}
