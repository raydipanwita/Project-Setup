from lib.todo_list import *

"""
Initially, there are no todos
And incomplete list is empty
"""

def test_no_todo():
    todolist = TodoList()
    assert todolist.incomplete() == []

"""

Initially, there are no todos
And complete list is empty
"""
def test_no_todo():
    todolist = TodoList()
    assert todolist.complete() == []