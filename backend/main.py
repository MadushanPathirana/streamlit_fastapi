from fastapi import FastAPI
from pydantic import BaseModel
import json


class User_input(BaseModel):
    name : str

app = FastAPI()

def printName(name):
    result ='hi '+ name
    return result

@app.post("/print")
def namePrinter(input:User_input):
    result =  printName(input.name)
    return result