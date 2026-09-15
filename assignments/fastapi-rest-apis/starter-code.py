from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Inventory API")


class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=0)


items_db = [
    {"id": 1, "name": "Laptop", "price": 999.99, "quantity": 3},
    {"id": 2, "name": "Mouse", "price": 29.99, "quantity": 10},
    {"id": 3, "name": "Keyboard", "price": 49.99, "quantity": 8},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items_db


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = next((item for item in items_db if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items")
def create_item(item: Item):
    # TODO: validate the item and add it to the in-memory database.
    # Hint: check whether the item already exists before inserting it.
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # TODO: find the item by id and update the record.
    # Hint: raise a 404 if the item does not exist.
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: remove the item from the list and return the deleted item or a success message.
    return {"message": "Item deleted"}
