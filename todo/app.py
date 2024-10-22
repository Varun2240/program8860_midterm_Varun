# app.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self):
        if not self.tasks:
            return "No tasks for today!"
        return "\n".join(self.tasks)


if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
            print(f"'{task}' added to the list.")
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo.remove_task(task)
            print(f"'{task}' removed from the list.")
        elif choice == '3':
            print("Tasks for today:")
            print(todo.show_tasks())
        elif choice == '4':
            break
        else:
            print("Invalid option, try again!")
