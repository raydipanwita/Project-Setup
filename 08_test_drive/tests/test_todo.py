from lib.todo import *

"""
When we construct with a task
We get that task reflected in the task property
"""

def test_construct_task_property():
    todo = Todo("Go shopping")
    assert todo.task == "Go shopping"

"""
When we construct 
The task is inititally incomplete
"""
def test_task_incomplete_first():
    todo = Todo("Go shopping")
    assert todo.complete == False

"""
When we mark a task as complete
It is complete
"""

def test_task_complete():
    todo = Todo("Go shopping")
    todo.mark_complete()
    assert todo.complete == True

# """
# When a task is completed
# The list is updated
# """

# def test_task_completd_list_updated():
#     tracker = Todo("Go Running")
#     tracker.mark_complete()
#     assert tracker.task == "Go Running"
    
# """
# When multiple tasks are added
# They are all added to the list of tasks
# And task mark as completed is added to the completed list
# """

# # tracker = TaskTracker()
# # tracker.add("Go Running")
# # tracker.add("Walk the dog")
# # tracker.add("Task out the trash")
# # tracker.mark_complete(1)
# # tracker.list_incomplete() = ["Walk the dog", "Task out the trash"]

# """
# If we try to mark a task complete that does not exist
# Raises an error
# """

# # tracker = TaskTracker()
# # tracker.add("Go Running")
# # tracker.mark_complete(-1) = Raises error "No such task exists"
# # tracker.list_incomplete() = ["Go Running"]

# """
# If we try to mark a task complete that does not exist(2nd)
# Raises an error
# """

# # tracker = TaskTracker()
# # tracker.add("walk the dog")
# # tracker.mark_complete(-1) = Raises error "No such task exists"
# # tracker.list_incomplete() = ["Walk the dog"]

# """
# When give up
# All tasks are marked as completed & removed from the list 
# """
# tracker = TaskTracker()
# tracker.add("Go Running")
# tracker.add("Walk the dog")
# tracker.add("Task out the trash")
# tracker.give_up()
# tracker.list_incomplete() = []
