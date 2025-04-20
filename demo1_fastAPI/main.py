from fastapi import FastAPI , Path , Request
import utils
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

@app.get("/")
def home():
    print(Request.method)
    return {"message": "Hello, World!"}

@app.get("/users/")
def getUsers():
    response = utils.fetchData()
    return response
@app.get("/users/{id}")
def getUser(id:int = Path( description="This is the ID of the user you want to fetch")):
    response = utils.fetchDataById(id)
    return response
@app.post("/users/")
def createUser(item:utils.Item):
    response = utils.createData(item.castToDict())
    return response
@app.put("/users/{id}")
def updateUser(* , id = int , item:utils.UpdateItem):
    print(id)
    print(item.__dict__)
    # response = utils.createData(item.castToDict())
    return ""