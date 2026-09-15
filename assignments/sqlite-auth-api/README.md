# 📘 Assignment: SQLite and Authentication API

## 🎯 Objective

Build a secure task-tracking API that stores information in SQLite and protects sensitive actions with basic authentication.

## 📝 Tasks

### 🛠️ Create the SQLite-backed API

#### Descrição
Create the FastAPI application and connect it to a SQLite database so the app can store and retrieve tasks.

#### Requisitos
O programa concluído deve:

- Create a FastAPI app with a clear title and description.
- Set up a SQLite database file named `tasks.db`.
- Define a task model with at least these fields: `id`, `title`, `description`, and `completed`.
- Expose a `GET /tasks` endpoint that returns all stored tasks in JSON format.
- Expose a `POST /tasks` endpoint that creates a new task and saves it to the database.
- Return a helpful validation error when required task fields are missing or empty.

### 🛠️ Add update and delete routes

#### Descrição
Expand the API so tasks can be edited or removed after they are created.

#### Requisitos
O programa concluído deve:

- Add a `PUT /tasks/{task_id}` endpoint to update an existing task.
- Add a `DELETE /tasks/{task_id}` endpoint to remove a task.
- Return `404` with a clear message when the task does not exist.
- Keep the database logic organized in separate helper functions or a simple data-access layer.
- Ensure the API responses remain JSON and use consistent field names.

### 🛠️ Protect the API with authentication

#### Descrição
Add a simple authentication layer so only authorized users can create, update, or delete tasks.

#### Requisitos
O programa concluído deve:

- Add a login route that validates a username and password or an API key.
- Require authentication on write actions such as `POST`, `PUT`, and `DELETE`.
- Read credentials from environment variables or a constant in the code.
- Use a header such as `X-API-Key` or `Authorization` to validate requests.
- Return `401` when a request is missing or has an invalid key.
- Include a short explanation on how to test the protected endpoints locally.

### ✅ Challenge Extension

#### Descrição
Take the project one step further by making the API more realistic for real-world use.

#### Requisitos
O programa concluído deve:

- Add optional filtering by completion status or task title.
- Support pagination for large task lists.
- Keep the database schema easy to extend for future features like users or categories.
- Explain how this app could evolve into a multi-user task manager.
