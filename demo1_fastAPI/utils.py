import json
from pydantic import BaseModel
from typing import Optional
def fetchData():
    try:
        with open('./data/users.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return "./data/users.json not found"
    except json.JSONDecodeError:
        return "Invalid JSON format in ./data/users.json"
def fetchDataById(id):
    try:
        with open('./data/users.json', 'r') as file:
            data = json.load(file)
            for x in data:
                if x["id"] == id:
                    return x
            return "user not found, check ID!"
    except FileNotFoundError:
        return "./data/users.json not found"
    except json.JSONDecodeError:
        return "Invalid JSON format in ./data/users.json"

def createData(data):
    response = fetchData()
    try:
        response.append(data)
        with open('./data/users.json', 'w') as file:
            json.dump(response, file, indent=4)
            return "User created successfully"
    except FileNotFoundError:
        return "./data/users.json not found"
    except json.JSONDecodeError:
        return "Invalid JSON format in ./data/users.json"
    
class Item(BaseModel):
    id :int 
    name: str
    age: int
    email: str
    def castToDict(self):
        return {"id": self.id , "name": self.name, "age": self.age , "email":self.email}
class UpdateItem(BaseModel):
    id :Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None