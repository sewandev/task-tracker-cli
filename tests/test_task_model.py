import unittest
import os
import json
from models.task_model import add_task, load_tasks, TASKS_FILE_PATH

class TestTaskModel(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TASKS_FILE_PATH):
            os.remove(TASKS_FILE_PATH)

    def test_add_task(self):
        """Prueba que la función add_task agrega una tarea correctamente."""

        test_task = {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "createdAt": "01-01-2023 00:00:00",
            "updatedAt": "Not updated yet"
        }

        add_task(test_task)
        tasks = load_tasks()

        self.assertEqual(len(tasks), 1) 
        self.assertEqual(tasks[0]["description"], "Test task")
        self.assertEqual(tasks[0]["status"], "todo") 

    def tearDown(self):
        if os.path.exists(TASKS_FILE_PATH):
            os.remove(TASKS_FILE_PATH)

if __name__ == '__main__':
    unittest.main()