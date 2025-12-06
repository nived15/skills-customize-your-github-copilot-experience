# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API for managing a library book catalog using the FastAPI framework. You'll learn how to create endpoints, handle HTTP methods, validate data, and work with modern Python web development tools.

## 📝 Tasks

### 🛠️	Create the Book API

#### Description
Build a FastAPI application that manages a collection of books with CRUD (Create, Read, Update, Delete) operations.

#### Requirements
Completed program should:

- Create a FastAPI application with at least 5 endpoints
- Implement GET endpoint to retrieve all books
- Implement GET endpoint to retrieve a single book by ID
- Implement POST endpoint to add new books with data validation
- Implement PUT endpoint to update existing book information
- Implement DELETE endpoint to remove books from the catalog
- Use Pydantic models for request/response validation
- Include proper HTTP status codes (200, 201, 404, etc.)


### 🛠️	Add Data Validation and Documentation

#### Description
Enhance your API with proper data validation, error handling, and automatic API documentation.

#### Requirements
Completed program should:

- Define Pydantic models with field validation (title, author, year, ISBN)
- Handle invalid requests with appropriate error messages
- Include path parameters and query parameters
- Add response models to endpoints
- Test the API using the auto-generated interactive documentation at `/docs`
- Include at least one endpoint with query filtering (e.g., search books by author)
