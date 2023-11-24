
class Task:
    def __init__(self, todo):
        self.todo  = todo
        self.complete = False

    def mark_complete(self):
        self.complete = True