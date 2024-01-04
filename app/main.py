from fastapi import FastAPI, Response, status, HTTPException
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
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data": f"not found : id = {id}"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found : id = {id}"
        )

    return {"data": post}


# title : str, content : str
@app.post("/v1/posts")
def create_post(payload: dict = Body(...)):  # take body, convert to a dict,
    print(payload)
    return {"status": f'success , title= {payload["title"]}'}


# title : str, content : str
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):  #  convert to pandantic Post model
    post_dict = post.dict()  # convert pandantic model to dict
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)

    return {"data": post_dict}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    for index, post in enumerate(my_posts):
        print("===========post id", post["id"])
        print("===========post id type", type(post["id"]))
        if post["id"] == id:
            my_posts.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"post not found , id = {id}"
    )


@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, post: Post):
    print(post)
    post_dict = post.dict()
    for index, current_post in enumerate(my_posts):
        if id == current_post["id"]:
            current_post["title"] = post_dict["title"]
            current_post["content"] = post_dict["content"]
            return {"data": current_post}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f" id not found : {id}"
    )
