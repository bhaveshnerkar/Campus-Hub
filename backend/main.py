
from fastapi import FastAPI
from backend.settings import settings

app = FastAPI(title="CampusHub API")


@app.get("/")
def home():
    return {"message": "CampusHub API is running successfully!"}


@app.get("/health")
def health_check():
    """Check whether the CampusHub API process is running."""
    return {"status": "ok"}
