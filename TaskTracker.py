class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                break

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def get_all_tasks(self):
        return self.tasks

# Create an instance of TaskTracker
task_tracker = TaskTracker()

# Add tasks
task_tracker.add_task("Finish project", "Complete the final report and submit it.", "2023-05-30")
task_tracker.add_task("Buy groceries", "Purchase fruits, vegetables, and milk.", "2023-05-20")
task_tracker.add_task("Call John", "Discuss the upcoming meeting.", "2023-05-25")

# Complete a task
task_tracker.complete_task("Buy groceries")

# Get a specific task
task = task_tracker.get_task("Finish project")
print("Task:", task.title)
print("Description:", task.description)
print("Due Date:", task.due_date)
print("Completed:", task.completed)

# Get all tasks
all_tasks = task_tracker.get_all_tasks()
print("\nAll Tasks:")
for task in all_tasks:
    print("Task:", task.title)
    print("Description:", task.description)
    print("Due Date:", task.due_date)
    print("Completed:", task.completed)
    print("--------------------")
