class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, tasks):
        self.tasks.append(tasks)

    def incomplete(self):
        return [
            task for task in self.tasks
            if not task.complete
        ]

    def complete(self):
        return [
            task for task in self.tasks
            if task.complete
        ]