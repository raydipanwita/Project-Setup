from lib.todo import *
from lib.todo_list import *

"""
When multiple tasks are added
They are all added to the list of tasks
"""

def test_multiple_task_added_list_updated():
    todolist = TodoList()
    task1 = Todo("Go Running")
    task2 = Todo("Walk the dog")
    task3 = Todo("Task out the trash")
    todolist.add(task1)
    todolist.add(task2)
    todolist.add(task3)
    assert todolist.incomplete() == [task1, task2, task3]

"""
When I add multiple tasks
And mark one as complete
It doe not show in the incomplete list anymore
"""

def test_task_marked_completed_incomplete_list_updated():
    todolist = TodoList()
    task1 = Todo("Go Running")
    task2 = Todo("Walk the dog")
    task3 = Todo("Task out the trash")
    todolist.add(task1)
    todolist.add(task2)
    todolist.add(task3)
    task1.mark_complete()
    assert todolist.incomplete() == [task2, task3]


"""
When I add multiple tasks
And mark one as complete
It shows in the complete list 
"""

def test_task_marked_completed_complete_list_updated():
    todolist = TodoList()
    task1 = Todo("Go Running")
    task2 = Todo("Walk the dog")
    task3 = Todo("Task out the trash")
    todolist.add(task1)
    todolist.add(task2)
    todolist.add(task3)
    task1.mark_complete()
    task2.mark_complete()
    assert todolist.complete() == [task1, task2]


# """
# When a task is marked as giveup
# All tasks are marked as completed
# """

# def test_for_give_up():
#     todolist = TodoList()
#     task1 = Todo("Go Running")
#     task2 = Todo("Walk the dog")
#     task3 = Todo("Task out the trash")
#     todolist.add(task1)
#     todolist.add(task2)
#     todolist.add(task3)
#     todolist.give_up()
#     assert todolist.incomplete() == []