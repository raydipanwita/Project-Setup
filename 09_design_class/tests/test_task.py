from lib.task import *


"""
When constructs with a title
"""
def test_constructs():
    task = Task("Walk the dog")
    assert task.todo == "Walk the dog"


"""
Newly constructed task are not compleye
"""
def test_constructs_incomplete_tasks():
    task = Task("Walk the dog")
    assert task.complete == False


"""
When I mark tasks as complete
It reflects in the complete property
"""
def test_constructs_incomplete_tasks():
    task = Task("Walk the dog")
    task.mark_complete ()
    assert task.complete == True

