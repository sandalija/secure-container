# Flask Todo List Application

A simple todo list application built with Flask and PostgreSQL, containerized with Docker.

## Features

- Create, read, update, and delete todos
- PostgreSQL database for persistent storage
- RESTful API endpoints
- Docker containerization

## API Endpoints

- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `PUT /todos/<id>` - Update a todo
- `DELETE /todos/<id>` - Delete a todo

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository
2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
3. The application will be available at `http://localhost:5000`

## Example API Usage

Create a new todo:
```bash
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete the project"}'
```

Get all todos:
```bash
curl http://localhost:5000/todos
```

Update a todo:
```bash
curl -X PUT http://localhost:5000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

Delete a todo:
```bash
curl -X DELETE http://localhost:5000/todos/1
``` 