class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)
        
    def incomplete(self):
        return [
            todo for todo in self.todos
            if todo.complete == False
        ]
    
    def complete(self):
        return[
            todo for todo in self.todos
            if todo.complete == True
        ]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete

        pass