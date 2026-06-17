from fastapi import FastAPI
from tasks import router as tasks_router

app = FastAPI(title="Task Tracker API")

app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Welcome to Task Tracker API. Use /tasks endpoint to manage your tasks."}
