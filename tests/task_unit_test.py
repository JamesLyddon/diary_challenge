from lib.task import *

"""
Given a description
We can create a task
"""
# task = Task("description")
# task.description # => "description"
# task.complete # => False

def test_initialisation():
    task = Task('walk the dog')
    assert isinstance(task, Task)
    assert task.description == 'walk the dog'
    assert task.complete == False