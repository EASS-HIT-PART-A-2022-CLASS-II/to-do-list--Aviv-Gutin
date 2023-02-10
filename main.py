import json
import redis
from fastapi import FastAPI
from redisjson import Client


r = redis.Redis()
redis_json = Client(r)
app = FastAPI()
TASKS_KEY = "tasks"


@app.get("/tasks")
def read_tasks():
   return redis_json.jsonget(TASKS_KEY, [])


@app.post("/tasks")
def create_task(task: str):
   tasks = redis_json.jsonget(TASKS_KEY, [])
   tasks.append({"task": task})
   redis_json.jsonset(TASKS_KEY, tasks)
   return {"task": task}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: str):
   tasks = redis_json.jsonget(TASKS_KEY, [])
   tasks[task_id] = {"task": task}
   redis_json.jsonset(TASKS_KEY, tasks)
   return {"task_id": task_id, "task": task}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
   tasks = redis_json.jsonget(TASKS_KEY, [])
   tasks.pop(task_id)
   redis_json.jsonset(TASKS_KEY, tasks)
   return {"task_id": task_id}