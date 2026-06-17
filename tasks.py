from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID
from enum import Enum
from datetime import datetime

router = APIRouter()

class TaskStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    completed = 'completed'

class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., max_length=200)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending
    due_date: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

fake_db: List[Task] = []

@router.get("/", response_model=List[Task])
def list_tasks():
    return fake_db

@router.post("/", response_model=Task)
def create_task(task: Task):
    fake_db.append(task)
    return task

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: UUID):
    for task in fake_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: UUID, task: Task):
    for idx, orig_task in enumerate(fake_db):
        if orig_task.id == task_id:
            task.updated_at = datetime.utcnow()
            fake_db[idx] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}")
def delete_task(task_id: UUID):
    for idx, task in enumerate(fake_db):
        if task.id == task_id:
            fake_db.pop(idx)
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
