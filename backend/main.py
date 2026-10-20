
from fastapi import FastAPI

app = FastAPI(title="CampusHub API")


@app.get("/")
def home():
    return {"message": "CampusHub API is running"}
