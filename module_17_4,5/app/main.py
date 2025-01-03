import uvicorn
import os
from fastapi import FastAPI

from backend.db import engine, Base,   SessionLocal
from routers import  user ,task
app=FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

Base.metadata.create_all(bind=engine)

if __name__=='__main__':
   uvicorn.run ('main:app') #--reload')
   #os.system ('pip install alembic')
   #os.system("alembic init migration")
   #os.system('alembic revision --autogenerate -m "Initial migration"')
   #os.system("alembic upgrade head")
   #os.system ('pip install python-slugify')
