from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

router = APIRouter(prefix="/tasks", tags=["tasks"])

class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: str = Field(..., regex="^(pending|in-progress|completed)$")
    due_date: Optional[date] = None

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: str = Field(..., regex="^(pending|in-progress|completed)$")
    due_date: Optional[date] = None

# In-memory storage for tasks
fake_db: List[Task] = []
next_id = 1  # auto-incrementing task id

@router.get("/", response_model=List[Task])
def list_tasks(status: Optional[str] = Query(None, regex="^(pending|in-progress|completed)$")):
    if status:
        return [task for task in fake_db if task.status == status]
    return fake_db

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_id
    # Create Task with auto-incremented ID
    new_task = Task(id=next_id, **task.dict())
    fake_db.append(new_task)
    next_id += 1
    return new_task

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

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for idx, task in enumerate(fake_db):
        if task.id == task_id:
            fake_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Task not found")
