from fastapi import APIRouter, HTTPException
from app.models import Item, ItemResponse
from app import database

router = APIRouter(prefix="/items", tags=["items"])

@router.post("",status_code=201)
def create_item(item: Item):
    new_item = item.dict()
    new_item["id"] = database.next_id
    database.items_db[database.next_id] = new_item
    database.next_id += 1
    return new_item


@router.get("")
def get_items():
    return list(database.items_db.values())

@router.get("/{item_id}")
def get_item(item_id: int):
    if item_id not in database.items_db:
        raise HTTPException(status_code=404, detail="Not found")
    return database.items_db[item_id]

@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in database.items_db:
        raise HTTPException(status_code=404, detail="Not found")
    updated = item.dict()
    updated["id"] = item_id
    database.items_db[item_id] = updated
    return updated

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in database.items_db:
        raise HTTPException(status_code=404, detail="Not found")
    del database.items_db[item_id]