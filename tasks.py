from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

router = APIRouter()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
    due_date: Optional[date] = None

fake_db: List[Task] = []

@router.get("/", response_model=List[Task])
def list_tasks():
    return fake_db

@router.post("/", response_model=Task)
def create_task(task: Task):
    fake_db.append(task)
    return task

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in fake_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    for idx, orig_task in enumerate(fake_db):
        if orig_task.id == task_id:
            fake_db[idx] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}")
def delete_task(task_id: int):
    for idx, task in enumerate(fake_db):
        if task.id == task_id:
            fake_db.pop(idx)
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
