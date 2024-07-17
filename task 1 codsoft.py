class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def list_tasks(self, filter_func=None, title=None):
        tasks = list(filter(filter_func, self.tasks)) if filter_func else self.tasks
        if not tasks:
            print(f"No {'tasks' if not title else title.lower()} in the list.")
            return
        print(f"\n{title or 'Tasks'}:")
        for i, task in enumerate(tasks, start=1):
            prefix = "[DONE] " if task.startswith("[DONE]") else " "
            print(f"{i}. {prefix}{task}")
    def modify_task(self, task_index, action):
        try:
            if action == 'mark':
                self.tasks[task_index - 1] = f"[DONE] {self.tasks[task_index - 1]}"
                print("Task marked as done.")
            elif action == 'remove':
                del self.tasks[task_index - 1]
                print("Task removed.")
        except IndexError:
            print("Invalid task index.")
todo_list = ToDoList()
while True:
    print("\nTo-Do List App")
    print("1. Add Task  2. List Tasks  3. Mark Task Done")
    print("4. Remove Task  5. Exit  6. Completed Tasks  7. Pending Tasks")
    choice = input("Enter your choice: ")
    if choice == '1':
        todo_list.add_task(input("Enter a new task: "))
        print("Task added successfully.")
    elif choice in ['2', '3', '4']:
        todo_list.list_tasks()
        if todo_list.tasks and choice != '2':
            index = int(input(f"Enter the task index to {'mark done' if choice == '3' else 'remove'}: "))
            todo_list.modify_task(index, 'mark' if choice == '3' else 'remove')
    elif choice == '5':
        break
    elif choice == '6':
        todo_list.list_tasks(lambda x: x.startswith("[DONE]"), "Completed Tasks")
    elif choice == '7':
        todo_list.list_tasks(lambda x: not x.startswith("[DONE]"), "Pending Tasks")
    else:
        print("Invalid choice.")
print("Exiting the To-Do List App.")
