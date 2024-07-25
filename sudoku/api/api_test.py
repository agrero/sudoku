from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4




# remodel 

# These are our connections to the frontend
# Should configure these in a file
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app = FastAPI()

# middleware for interacting with javascript frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

tasks = []

class Task(BaseModel):
    id: Optional[UUID] = None         # Optional, default value
    title: str                        # Mandatory, no default value
    description: Optional[str] = None # Optional, default value
    completed: bool = False           # Mandatory, default value

# ok for these to go to the same endpoint 
# so long as they are returning different tasks
@app.post('/tasks/', response_model=Task)
def create_task(task: Task):

    # does this overwrite the task id
    task.id = uuid4() # automatically create uuid taskid

    tasks.append(task) # append task to the list
    return task

@app.get('/tasks/', response_model=List[Task])
def read_tasks():
    return tasks

@app.get('/tasks/{task_id}', response_model=Task)
def read_task(task_id: UUID):
    for task in tasks: 
        if task.id == task_id:
            return task
        
    raise HTTPException(status_code=404, detail='Task not found')

@app.put('/tasks/{task_id}', response_model=Task)
def update_task(task_id:UUID, task_update: Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[idx] = updated_task
            return updated_task
        
    raise HTTPException(status_code=404, detail='Task not found')

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
        
    raise HTTPException(status_code=404, detail='Task not found')

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port = 8000)