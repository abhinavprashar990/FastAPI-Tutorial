<<<<<<< HEAD
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
=======
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit,published:bool=True, sort: Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the db'}  
    else:
        return {'data':f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/info')
def info():
    return {'data':'all info blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return limit
     
class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]
    
@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f'Blog is created with title as {request.title}'}
    

# if __name__ == '__main__':
#         uvicorn.run(app, host="127.0.0.1", port = 9000)
        
>>>>>>> f1b6870 (Initial Commit)
