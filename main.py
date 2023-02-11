import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uuid
import redis
from datetime import date
from dataclasses import dataclass, asdict
from json import dumps


app = FastAPI()
r = redis.Redis(host="redis", port=6379)


@dataclass
class Task:
     # Indexed for exact text matching
    task_name: str
    task_status: str
    task_due_date: date
    @property
    def __dict__(self):
        """
        get a python dictionary
        """
        return asdict(self)

    @property
    def json(self):
        """
        get the json formated string
        """
        return dumps(self.__dict__)


# Create a new task.
@app.post("/tasks/")
def create_task(task: Task):
    new_task = json.dumps(asdict(task))
    r.set(str(uuid.uuid4()), new_task)
    return {}


#update task
@app.put("/task/{item_id}")
async def read_item(item_id: str, task: Task):
    new_task = json.dumps(asdict(task))
    task = r.set(item_id, new_task)
    return {"update": task}


#delete task

@app.delete("/task/{item_id}")
async def read_item(item_id: str):
    task = r.delete(item_id)
    return {"update": task}


#get task
@app.get("/task/{item_id}")
async def read_item(item_id):
    task = r.get(item_id)
    return {"task": json.loads(task)}


#get all tasks
@app.get("/tasks")
async def read_item():
    tasks = r.keys()
    res = []
    for key in tasks:
        task = json.loads(r.get(key))
        task["id"] = key
        res.append(task)
    return res
