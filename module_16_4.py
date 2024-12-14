import uvicorn
from fastapi import FastAPI,  HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled":True})
users = [ ]

class User(BaseModel):
    id:int =Field(...,ge=1)
    username: str = Field(..., min_length=5, max_length=100, description="user name")
    age: int = Field(..., ge=18, le=120)

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username:str, age:int):
    new_id=max((user.id for user in users), default=0)+1
    new_user=User(id=new_id, username=username, age=age)
    users.append(new_user)
    return  new_user

@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id:int, username:str, age:int):
    for user in users:
        if user.id==user_id:
            user.username=username
            user.age=age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id:int):
    for i, user in enumerate(users):
        if user.id==user_id:
            user_del=users.pop(i)
            return user_del
    raise HTTPException(status_code=404, detail="User was not found")


if __name__=='__main__':
    uvicorn.run ('module_16_4:app') #,  --reload