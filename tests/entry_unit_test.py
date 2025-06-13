from lib.entry import *

"""
Given a title and content
We can create an Entry
"""
# entry = Entry("title", "content")
# entry.title # => "title"
# entry.content # => "content"

def test_initialisation():
    entry = Entry('title', 'content')
    assert isinstance(entry, Entry)
    assert entry.title == 'title'
    assert entry.content == 'content'