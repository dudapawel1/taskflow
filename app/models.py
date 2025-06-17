from datetime import datetime

class Task:
    def __init__(self, title, description, deadline, completed=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def is_overdue(self):
        return not self.completed and datetime.now() > self.deadline

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def get_tasks_by_status(self, completed=True):
        return [task for task in self.tasks if task.completed == completed]
