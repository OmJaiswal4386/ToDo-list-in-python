class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "[ ]"
                if task["done"]:
                    status = "[X]"
                print(f"{index}. {status} {task['task']}")

    def mark_task_done(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    while True:
        print("\nTODO LIST APP")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done: "))
            todo_list.mark_task_done(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
