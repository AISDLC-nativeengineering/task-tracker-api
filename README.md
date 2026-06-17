# Task Tracker API

A REST API built with Python FastAPI for managing tasks and to-do lists. Supports CRUD operations for tasks with fields: title, description, status, and due date.

## Features & Enhancements

- Task CRUD (Create, Read, Update, Delete)
- Field support: Title, Description, Status, Due Date
- Filtering tasks by status and due date
- Pagination support for task lists
- Error handling and validation
- Planned: User authentication & authorization
- Planned: Webhook for task updates
- Planned: Export tasks to CSV

## API Endpoints (Examples)

- `GET /tasks` — List all tasks
- `POST /tasks` — Create a new task
- `GET /tasks/{id}` — Retrieve task details
- `PUT /tasks/{id}` — Update a task
- `DELETE /tasks/{id}` — Delete a task

## Installation

```bash
git clone https://github.com/AISDLC-nativeengineering/task-tracker-api.git
cd task-tracker-api
pip install -r requirements.txt
uvicorn main:app --reload
```

## Usage

Access the API at `http://localhost:8000` and interact with endpoints via Swagger UI at `http://localhost:8000/docs`.

## Contribution

Pull requests and issue reports are welcome! Please follow standard Python style guides.

## License

MIT License.  
See the [LICENSE](LICENSE) file for full license text.
