import pytest
import json
from fastapi import FastAPI
from fastapi.testclient import TestClient
from datetime import date

@pytest.fixture
def client():
    app = FastAPI()
    client = TestClient(app)
    return client

def test_create_task(client):
    task = {
        "task_name": "Test task",
        "task_status": "Active",
        "task_due_date": date(2023, 2, 11),
    }
    response = client.post("/tasks/", json=task)
    assert response.status_code == 200

def test_update_task(client):
    task = {
        "task_name": "Test task",
        "task_status": "Active",
        "task_due_date": date(2023, 2, 11),
    }
    task_name = ""
    response = client.put(f"/task/{task_name}", json=task)
    assert response.status_code == 200

def test_delete_task(client):
    task_id = ""
    response = client.delete(f"/task/{task_id}")
    assert response.status_code == 200

def test_get_task(client):
    task_id = ""
    response = client.get(f"/task/{task_id}")
    assert response.status_code == 200

def test_get_all_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200