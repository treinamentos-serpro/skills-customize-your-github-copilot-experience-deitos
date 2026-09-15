from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Task Tracker API")
DATABASE_PATH = "tasks.db"
API_KEY = "change-me"


class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool = False


class Task(TaskBase):
    id: int


def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        conn.commit()


def require_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return x_api_key


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    with get_db_connection() as conn:
        rows = conn.execute(
            "SELECT id, title, description, completed FROM tasks ORDER BY id"
        ).fetchall()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "description": row["description"],
            "completed": bool(row["completed"]),
        }
        for row in rows
    ]


@app.post("/tasks")
def create_task(task: TaskBase, api_key: str = require_api_key):
    with get_db_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
            (task.title, task.description, int(task.completed)),
        )
        conn.commit()
        task_id = cursor.lastrowid

    return {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
    }


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskBase, api_key: str = require_api_key):
    with get_db_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
            (task.title, task.description, int(task.completed), task_id),
        )
        conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, api_key: str = require_api_key):
    with get_db_connection() as conn:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": f"Task {task_id} deleted successfully"}
