import json
from fastapi import FastAPI

app = FastAPI()


def get_tasks():
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    return tasks


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


@app.get("/tasks")
def read_tasks():
    return get_tasks()


@app.post("/tasks")
def create_task(task: str):
    tasks = get_tasks()
    tasks.append({"task": task})
    save_tasks(tasks)
    return {"task": task}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: str):
    tasks = get_tasks()
    tasks[task_id] = {"task": task}
    save_tasks(tasks)
    return {"task_id": task_id, "task": task}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = get_tasks()
    tasks.pop(task_id)
    save_tasks(tasks)
    return {"task_id": task_id}