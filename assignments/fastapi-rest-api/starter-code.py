# FastAPI REST API Starter Code
# Install required packages: pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Library Book API", version="1.0.0")

# TODO: Define your Pydantic models here
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    isbn: Optional[str] = None

# In-memory storage (replace with database in real applications)
books_db = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "isbn": "978-0-06-112008-4"},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "isbn": "978-0-452-28423-4"},
]

# TODO: Implement your API endpoints below

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Library Book API"}

# TODO: Add GET /books endpoint to retrieve all books

# TODO: Add GET /books/{book_id} endpoint to retrieve a single book

# TODO: Add POST /books endpoint to create a new book

# TODO: Add PUT /books/{book_id} endpoint to update a book

# TODO: Add DELETE /books/{book_id} endpoint to delete a book

# To run the server, use: uvicorn starter-code:app --reload
