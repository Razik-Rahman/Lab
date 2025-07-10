from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create a FastAPI app
app = FastAPI()

# In-memory "database"
fake_db = {}

# Define a data model for an Item
class Item(BaseModel):
    name: str
    price: float

# 1️⃣ POST – Create a new item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item_id] = item
    return {"message": "Item created", "item": item}

# 2️⃣ GET – Retrieve an existing item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

# 3️⃣ PUT – Update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return {"message": "Item updated", "item": item}

# 4️⃣ DELETE – Delete an existing item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"message": "Item deleted"}
