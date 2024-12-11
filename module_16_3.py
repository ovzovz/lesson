import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = [ {'user_id':1, 'user_info': 'Имя: Example, возраст: 18'}]


@app.get("/users")
async def get_users():
    return {user['user_id']: user['user_info'] for user in users}

@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(min_length=2,
                               description="Enter username")]
                    ,age:Annotated[int, Path(ge=18,le=120,
                               description="Enter age")]):
    new_id=max(user['user_id'] for user in users)+1 if users else 1
    new_user={"user_id": new_id, "user_info":f'Имя: {username}, возраст:{age}'}
    users.append(new_user)
    return  f'User {new_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id:Annotated[int, Path(ge=1)],
                      username: Annotated[str,Path(min_length=2,
                               description="Enter username")],
                    age:Annotated[int, Path(ge=18,le=120,
                               description="Enter age")]):
    for user in users:
        if user["user_id"]==user_id:
            user['user_info'] = f"Имя: {username}, возраст: {age}"
            return f"The user {user_id} has been updated"
    return f'User {user_id} not found'

@app.delete('/user/{user_id}')
async def delete_user(user_id:Annotated[int, Path(ge=1)]):
    for i, user in enumerate(users):
        if user["user_id"]==user_id:
            del users[i]
            return f"User {user_id} has been deleted"
    return f'User {user_id} not found'



if __name__=='__main__':
    uvicorn.run ('module_16_3:app') #,  --reload