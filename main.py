from typing import Optional
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel
from typing import List


app = FastAPI()


@app.get('/blog')
def index(limit=50, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs for the db"}
    else:
        return {"data": f"{limit} blogs for the db"}


@app.get('/blog/{id}')
def about(id: int):
    return {"data": id}


@app.get('/blog/{id}/comments')
def about(id, limit=16):
    return {"data": {"1", "2", f"{limit} comments"}}


# query parametere
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {
    "item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# path parameter


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    # return request
    return {'data': f'Blog is Created with title {blog.title}'}


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
   MAIL_USERNAME="milans.tagline@gmail.com",
   MAIL_PASSWORD="tagline@123",
   MAIL_FROM = "milans.tagline@gmail.com",
   MAIL_PORT=587,
   MAIL_SERVER="smtp.gmail.com",
   MAIL_TLS=True,
   MAIL_SSL=False
)


html = """
<p>Hi this test mail, thanks for using Fastapi-mail</p> 
"""


@app.post("/email")
async def simple_send(email: EmailSchema):

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=["rootmilan123@gmail.com"],
        body=html,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
