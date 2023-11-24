from lib.tasklist import *
from lib.task import *

"""
When multiple tasks are added
They are all added to the incomplete list of tasks
"""
def test_adds_and_listupdated_for_incomplete():
    tracker = TaskList()
    task1 = Task("Go Running")
    task2 = Task("Walk the dog")
    task3 = Task("Task out the trash")
    tracker.add(task1)
    tracker.add(task2)
    tracker.add(task3)
    assert tracker.incomplete() == [task1, task2, task3]

"""
When multiple tasks are added
And mark 1 as complete
They are all added to the incomplete list of tasks
"""
def test_marked_todo_complete_removed_from_incomplete_list():
    tracker = TaskList()
    task1 = Task("Go Running")
    task2 = Task("Walk the dog")
    task3 = Task("Task out the trash")
    tracker.add(task1)
    tracker.add(task2)
    tracker.add(task3)
    task2.mark_complete()
    assert tracker.incomplete() == [task1, task3]

"""
When multiple tasks are added
And mark 1 as complete
They are all added to the list of tasks
"""

def test_marked_todo_complete_added_to_completed_list():
    tracker = TaskList()
    task1 = Task("Go Running")
    task2 = Task("Walk the dog")
    task3 = Task("Task out the trash")
    tracker.add(task1)
    tracker.add(task2)
    tracker.add(task3)
    task2.mark_complete()
    assert tracker.complete() == [task2 ]

