from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

todos = [
    {
        'id': '1',
        'item': 'read a book.'
    },
    {
        'id': '2',
        'item': 'cycle around town'
    }
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/todo', tags=['todos'])
async def get_todos() -> dict:
    return {'data' : todos}

@app.get("/", tags=['root'])
async def read_root() -> dict:
    return {'message' : 'welcome to your app'}

# this should be a pydantic model
@app.post("/todo", tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        'data' : 'todo added'
    } 

@app.put("/todo/{id}", tags=["todo"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['item'] = body['item']
            return {
                'data' : f'todo with id {id} has been updated'
            }
    return {
        'data' : f'Todo with id {id} not found'
    }