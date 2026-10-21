
from fastapi import FastAPI
from backend.settings import settings
app = FastAPI(title="CampusHub API")


@app.get("/")
def home():
    return {"message": "CampusHub API is running successfully!"}
