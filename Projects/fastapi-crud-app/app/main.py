from fastapi import FastAPI
from app.router import items

app = FastAPI(title="Simple CRUD Application")

app.include_router(items.router)

@app.get("/")
def root():
    return {"message":"API is running"}