import uvicorn
from fastapi import FastAPI,  Path, HTTPException, Request
from fastapi.responses import  HTMLResponse
from pydantic import BaseModel
from typing import Annotated
from fastapi.templating import Jinja2Templates
#from starlette.requests import Request

templates=Jinja2Templates(directory="templates")

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled":True})
users = [ ]

class User(BaseModel):
    id:int
    username: str
    age: int

@app.get("/")
def get_main_page(request:Request) ->HTMLResponse:
    return templates.TemplateResponse("users.html",{"request":request, "users":users})


@app.get(path="/user/{user_id}")
def get_users(request:Request, user_id:int)->HTMLResponse:
    for user in users:
        if user.id==user_id:
            return templates.TemplateResponse("users.html",{"request":request, "user":user})
    raise HTTPException(status_code=404, detail="user not found")

@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id:Annotated[int, Path(ge=1)]):
    for i, user in enumerate(users):
        if user.id==user_id:
            user_del=users.pop(i)
            return user_del
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}", response_model=User)
async def post_user(username: Annotated[str, Path(min_length=2,
                               description="Enter username")]
                    ,age:Annotated[int, Path(ge=18,le=120,
                               description="Enter age")]):
    new_id=max((user.id for user in users), default=0)+1
    new_user=User(id=new_id, username=username, age=age)
    users.append(new_user)
    return  new_user

@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id:Annotated[int, Path(ge=1)],
                      username: Annotated[str,Path(min_length=2,
                               description="Enter username")],
                    age:Annotated[int, Path(ge=18,le=120,
                               description="Enter age")]):
    for user in users:
        if user.id==user_id:
            user.username=username
            user.age=age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

if __name__=='__main__':
    uvicorn.run ('module_16_5:app') #,  --reload