# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with FastAPI, define request and response models, and implement basic CRUD operations for real-world data.

## 📝 Tasks

### 🛠️ Create the API App

#### Descrição
Build the initial FastAPI application and configure a simple in-memory data store for products or tasks.

#### Requisitos
O programa concluído deve:

- Create a FastAPI app instance with a meaningful title.
- Define at least one data model using Pydantic.
- Expose a health check endpoint at `/health` returning a JSON status.
- Return a list of items from a `GET /items` endpoint.
- Return a single item by ID from a `GET /items/{item_id}` endpoint.

### 🛠️ Add CRUD Endpoints

#### Descrição
Expand the API to support creating, updating, and deleting records with validation.

#### Requisitos
O programa concluído deve:

- Add a `POST /items` endpoint to create a new item.
- Validate incoming data using a Pydantic model.
- Add a `PUT /items/{item_id}` endpoint to update an existing item.
- Add a `DELETE /items/{item_id}` endpoint to remove an item.
- Return `404` with a clear message when an item is not found.

### 🛠️ Document and Test the API

#### Descrição
Use FastAPI's built-in documentation tools and verify that the API responds correctly to client requests.

#### Requisitos
O programa concluído deve:

- Access the automatic Swagger UI at `/docs`.
- Keep the API responses in JSON format.
- Use descriptive field names and validation rules.
- Test the endpoints using the FastAPI test client or by running the app locally.
- Include a short explanation in comments or documentation describing each endpoint's purpose.

### ✅ Challenge Extension

#### Descrição
Take the API one step further by adding filters, sorting, or search functionality.

#### Requisitos
O programa concluído deve:

- Add a query parameter to filter items by name or category.
- Support optional sorting or return only items that match a filter.
- Keep the code organized with clear function names and reusable logic.
- Explain how the API would scale to a real database-backed application.
