# Task Manager CLI

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A simple **Command Line Interface (CLI)** Task Manager built with Python. This project is part of the challenge [Task Tracker CLI](https://roadmap.sh/projects/task-tracker) from roadmap.sh.

## Overview

The **Task Manager CLI** is a Python-based application that allows users to manage tasks from the command line. It follows the **Model-View-Controller (MVC)** architecture, ensuring a clean separation of concerns and making the codebase maintainable and scalable.

This project is designed to help users:
- Create, update, and delete tasks.
- Mark tasks as "todo," "in-progress," or "done."
- List tasks with optional status filtering.

---

## Features

- **Add Tasks**: Create new tasks with a description.
- **Update Tasks**: Modify the description or status of existing tasks.
- **Delete Tasks**: Remove tasks by their ID.
- **List Tasks**: View all tasks or filter them by status (`todo`, `in-progress`, `done`).
- **Interactive CLI**: User-friendly command-line interface with helpful prompts.
- **Data Persistence**: Tasks are saved in a JSON file (`data/tasks.json`) for persistence across sessions.

---

## Installation

### Prerequisites

- Python 3.x
- Git (optional)

### Steps

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/your-username/task-manager-cli.git
   cd task-manager-cli
   ```

2. **Run the application**:
   ```bash
   python task_cli.py
   ```
---

## Usage
### Available Commands
**Command	Description**

```bash
- add <description>	Create a new task with the given description.
- update <id> <description>	Update the description of an existing task.
- delete <id>	Delete a task by its ID.
- mark-in-progress <id>	Mark a task as "in-progress."
- mark-done <id>	Mark a task as "done."
- list	List all tasks.
- list <status>	List tasks filtered by status (todo, in-progress, done).
- help	Display the list of available commands.
- exit	Exit the application.
```
