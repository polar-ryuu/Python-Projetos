from fastapi import FastAPI

app = FastAPI()

items =[]
inventory = { 1: {"type": "milk", "quantity": 10}}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"Data": "About"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]