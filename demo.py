from fastapi import FastAPI
from streamlit import success

app=FastAPI()

todos=[
    {'id':1,'task':'drink water'}
]

@app.get('/get/{todo_id}')
def getrequest(todo_id:int):
    for todo in todos:
        if todo['id']==todo_id:
            return {'result':todo}
@app.get('/getall')
def getall():
    return {'resut':todos}

@app.post('/post/todo')
def  post_todo(todo:dict):

    if todos:
        new_todo={
            'id':max(todo['id'] for todo in todos)+1,
            'task':todo['task']
        }
    else:
        new_todo = {
            'id': 1,
            'task': todo['task']
        }


    todos.append(new_todo)


@app.put('/put/{id}')
def put_todo(id:int,put_todo:dict):
    for todo in todos:
        if todo['id']==id:
            todo['id']=put_todo['id']
            todo['task']=put_todo['task']

@app.delete('/del/{id}')
def delete_todo(id:int):
    for i in range(len(todos)):
        if todos[i]['id']==id:
            todos.pop(i)







