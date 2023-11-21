from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Cat(BaseModel):
    name: str
    age: int
    breed: str
    status: str

cats_db = []

@app.post("/cats/", response_model=Cat)
def add_cat(cat: Cat):
    cats_db.append(cat)
    return cat

@app.get("/cats/", response_model=List[Cat])
def view_cats():
    return cats_db

@app.put("/cats/{cat_id}/", response_model=Cat)
def update_cat(cat_id: int, cat: Cat):
    cats_db[cat_id - 1] = cat
    return cat

@app.delete("/cats/{cat_id}/", response_model=Cat)
def delete_cat(cat_id: int):
    deleted_cat = cats_db.pop(cat_id - 1)
    return deleted_cat

@app.get("/cats/find/", response_model=List[Cat])
def find_cat_by_name(name: str):
    found_cats = [cat for cat in cats_db if name.lower() in cat.name.lower()]
    return found_cats
