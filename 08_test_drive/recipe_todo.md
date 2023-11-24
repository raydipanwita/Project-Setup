# Follow the design recipe to implement the following user story in your project:

## 1. Describe the Problem

>As a user
>So that I can keep track of my tasks
>I want to check if a text includes the string #TODO.


## 2. Design the Class Interface

#_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE
```python
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass
```

## 3. Create Examples as Tests

Class ToDoList:-
"""
First, there are no tasks
"""

# tracker = TaskTracker()
# tracker.list_incomplete() = []

"""
When a task is added
The list is updated
"""

# tracker = TaskTracker()
# tracker.add("Go Running")
# tracker.list_incomplete() = ["Go Running"]

"""
When multiple tasks are added
They are all added to the list of tasks
"""

# tracker = TaskTracker()
# tracker.add("Go Running")
# tracker.add("Walk the dog")
# tracker.add("Task out the trash")
# tracker.list_incomplete() = ["Go Running", "Walk the dog", "Task out the trash"]


"""
When multiple tasks are added
They are all added to the list of tasks
And task mark as completed is removed from the list
"""

# tracker = TaskTracker()
# tracker.add("Go Running")
# tracker.add("Walk the dog")
# tracker.add("Task out the trash")
# tracker.mark_complete(1)
# tracker.list_incomplete() = ["Walk the dog", "Task out the trash"]

"""
If we try to mark a task complete that does not exist
Raises an error
"""

# tracker = TaskTracker()
# tracker.add("Go Running")
# tracker.limark_complete(-1) = Raises error "No such task exists"
# tracker.list_incomplete() = ["Go Running"]

"""
If we try to mark a task complete that does not exist(2nd)
Raises an error
"""

# tracker = TaskTracker()
# tracker.add("walk the dog")
# tracker.mark_complete(-1) = Raises error "No such task exists"
# tracker.list_incomplete() = ["Walk the dog"]

"""
When give up
All tasks are marked as completed & removed from the list 
"""
# tracker = TaskTracker()
# tracker.add("Go Running")
# tracker.add("Walk the dog")
# tracker.add("Task out the trash")
# tracker.give_up()
# tracker.list_incomplete() = []


Class TODO:
"""
When 

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

