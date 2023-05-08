from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

homeworks = {
    1: {
        "title":"Mobile Legends",
        "description":"reach mythical glory rank",
        "progress":"On Progress"
    },
    2: {
        "title":"WADS",
        "description":"making RestAPI",
        "progress":"not started yet"
    },
    3:{
        "title":"Sports",
        "description":"ride bicyle in park",
        "progress":"finished"
    }
}


class Homework(BaseModel):
    title = str
    description = str
    progress = str

class UpdateHomework(BaseModel):
    title : Optional[str] = None
    description : Optional[str] = None
    progress : Optional[str] = None

@app.get("/")
def index():
    return {"Message": "Reynard's Homework"}


@app.get("/get-homework/{homework_id}")
def get_homework(homework_id: int):
    return homeworks[homework_id]

@app.get("/get-homework_by_title/{homework_id}")
def get_homework(title: str):
    for homework_id in homeworks:
        if homeworks[homework_id]["title"] == title:
            return homeworks[homework_id]
    return {"Error": "There is no homework that you are looking for"}

@app.post("/create-homework/{homework_id}")
def add_homework(homework_id: int, homework:Homework):
    if homework_id in homeworks:
        return{"Error": "You have added that kind of homework"}
    homeworks[homework_id] = homework
    return homeworks[homework_id]

@app.put("/update-homework/{homework_id}")
def update_homework(homework_id: int, homework:UpdateHomework):
    if homework_id not in homeworks:
        return{"Error":"You do not have that much homework"}
    
    if homeworks[homework_id].title != None:
        homeworks[homework_id].title = homework.title

    if homeworks[homework_id].description != None:
        homeworks[homework_id].description = homework.description

    if homeworks[homework_id].progress != None:
        homeworks[homework_id].progress = homework.progress

    return homeworks[homework_id]

@app.delete("/delete-homework/{homework_id}")
def delete_homework(homework_id: int):
    del homeworks[homework_id]
    return{"Update": "Homework has been deleted"}