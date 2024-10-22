# test_app.py

from todo.app import ToDoList


def test_add_task():
    todo = ToDoList()
    todo.add_task("Task 1")
    assert "Task 1" in todo.tasks

def test_remove_task():
    todo = ToDoList()
    todo.add_task("Task 1")
    todo.remove_task("Task 1")
    assert "Task 1" not in todo.tasks

def test_show_tasks_empty():
    todo = ToDoList()
    assert todo.show_tasks() == "No tasks for today!"

def test_show_tasks_with_items():
    todo = ToDoList()
    todo.add_task("Task 1")
    assert todo.show_tasks() == "Task 1"
