
# CampusHub Backend

Python backend built with FastAPI.

## Requirements

- Python 3.10 or newer

## Local setup

Open a terminal in the `backend` directory.

Create a virtual environment:

    python -m venv .venv

Activate it on Windows:

    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

Start the API server:

    uvicorn main:app --reload

Open http://127.0.0.1:8000 to check the API.

Open http://127.0.0.1:8000/docs to explore the API endpoints.
