from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_read_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_create_task(client):
    response = client.post("/tasks", json={"task": "test task"})
    assert response.status_code == 200
    assert response.json() == {"task": "test task"}

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == [{"task": "test task"}]


def test_update_task(client):
    # Create a new task first
    client.post("/tasks", json={"task": "test task"})

    response = client.put("/tasks/0", json={"task": "updated test task"})
    assert response.status_code == 200
    assert response.json() == {"task_id": 0, "task": "updated test task"}

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == [{"task": "updated test task"}]


def test_delete_task(client):
    # Create a new task first
    client.post("/tasks", json={"task": "test task"})

    response = client.delete("/tasks/0")
    assert response.status_code == 200
    assert response.json() == {"task_id": 0}

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []