class ToDoList:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def list_tasks(self):
    if not self.tasks:
      print("There are no tasks in the list.")
      return
    for i, task in enumerate(self.tasks, start=1):
      prefix = "[DONE] " if task.startswith("[DONE]") else "* "
      print(f"{i}. {prefix}{task}")

  def mark_done(self, task_index):
    try:
      self.tasks[task_index - 1] = f"[DONE] {self.tasks[task_index - 1]}"
      print("Task marked as done.")
    except IndexError:
      print("Invalid task index.")

  def remove_task(self, task_index):
    try:
      del self.tasks[task_index - 1]
      print("Task removed.")
    except IndexError:
      print("Invalid task index.")

  def show_completed_tasks(self):
    completed_tasks = [task for task in self.tasks if task.startswith("[DONE]")]
    self._print_tasks(completed_tasks, "Completed Tasks")

  def show_incomplete_tasks(self):
    incomplete_tasks = [task for task in self.tasks if not task.startswith("[DONE]")]
    self._print_tasks(incomplete_tasks, "Incomplete Tasks")

  def _print_tasks(self, tasks, title):
    if not tasks:
      print(f"There are no {title.lower()} in the list.")
      return
    print(f"\n{title}:")
    for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")

# Create a to-do list object
todo_list = ToDoList()

# Main loop for user interaction
while True:
  print("\nTo-Do List App")
  print("1. Add Task")
  print("2. List Tasks")
  print("3. Mark Task Done")
  print("4. Remove Task")
  print("5. Exit")
  print("6. Show Completed Tasks")
  print("7. Show Incomplete Tasks")

  choice = input("Enter your choice: ")

  if choice == '1':
    task = input("Enter a new task: ")
    todo_list.add_task(task)
    print("Task added successfully.")
  elif choice == '2':
    todo_list.list_tasks()
  elif choice == '3':
    todo_list.list_tasks()
    if todo_list.tasks:
      task_index = int(input("Enter the task index to mark done: "))
      todo_list.mark_done(task_index)
  elif choice == '4':
    todo_list.list_tasks()
    if todo_list.tasks:
      task_index = int(input("Enter the task index to remove: "))
      todo_list.remove_task(task_index)
  elif choice == '5':
    break
  elif choice == '6':
    todo_list.show_completed_tasks()
  elif choice == '7':
    todo_list.show_incomplete_tasks()
  else:
    print("Invalid choice.")

print("Exiting the To-Do List App.")
