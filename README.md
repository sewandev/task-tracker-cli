# Task Tracker CLI

## Overview
Task Tracker CLI is a command-line application that helps users manage tasks efficiently. This project allows users to add, update, delete, and list tasks, offering a simple way to track ongoing activities using Python. The project follows an MVC (Model-View-Controller) architecture for better code organization and maintainability.

Tasks are stored in a JSON file and can have different statuses such as `todo`, `in-progress`, and `done`. Users can interact with the application via command-line commands, making it a lightweight and effective solution for task management.

Source Challenge [Roadmap.sh](https://roadmap.sh/projects/task-tracker)

---

## Features

- Add new tasks with descriptions.
- Update existing tasks.
- Mark tasks as `in-progress` or `done`.
- Delete tasks by ID.
- List tasks by status or view all tasks.

---

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sewandev/task-tracker-cli
   cd task-tracker-cli
   ```

2. Execute from console:
   ```bash
   python task-cli.py
   ```

---

### Example Usage

#### Adding a new task
```bash
# Adds a new task with the given description.
add Buy groceries
```

#### Updating a task description
```bash
# Updates the description of a task by ID.   
update 1 "Complete the project report"
```

#### Deleting a task
```bash
# Deletes a task by ID.    
delete 2
```

#### Listing all tasks
```bash
# Lists all tasks.
list
```

#### Listing tasks by status
```bash
# Lists tasks by status (todo, in-progress, done).
list done
list in-progress
list todo
```

---

## Project Structure

```
project-root/
│-- controllers/
│   ├── task_controller.py
│-- models/
│   ├── task_model.py
│-- views/
│   ├── task_view.py
│-- task-cli.py
│-- README.md
```

- **controllers/** - Handles application logic.
- **models/** - Manages data and JSON file operations.
- **views/** - Handles user interactions.
- **task-cli.py** - The main entry point for the CLI application.

---

## Contributing

If you'd like to contribute to the project, feel free to fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License.