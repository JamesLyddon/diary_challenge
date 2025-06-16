from lib.diary import *
from lib.contact import *
from lib.entry import *
from lib.task import *

def test_initialisation():
    diary = Diary()
    assert isinstance(diary, Diary)

"""
Given a Diary
We can add entries
And retrieve those entries
"""
def test_add_retrieve_entries():
    diary = Diary()
    entry_1 = Entry('title_1', '1 2 3')
    entry_2 = Entry('title_2', '1 2 3 4 5 6')
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    assert diary.get_all_entries() == [entry_1, entry_2]

"""
Given a Diary
We can add tasks
And retrieve those tasks
"""
def test_add_tasks():
    diary = Diary()
    task_1 = Task('walk the dog')
    task_2 = Task('feed the cat')
    diary.add_task(task_1)
    diary.add_task(task_2)
    assert diary.get_all_tasks() == [task_1, task_2]

# """
# Given a Diary
# We can add entries with phonenumber and they will be parsed and saved
# We can then retrieve any saved contact details
# """
def test_phone_numbers_scraped_from_entries():
    diary = Diary()
    entry_1 = Entry('title_1', 'content_1 Pete: 570-560-7834')
    entry_2 = Entry('title_2', 'content_2')
    entry_3 = Entry('title_2', 'content_3 call Sally 07986756243')
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_3)
    assert diary.get_all_contacts() == [{'name': 'Pete', 'number': '570-560-7834'}, {'name': 'Sally', 'number': '07986756243'}]

# """
# Given a Diary
# We can add entries
# We can provide a time and wpm
# And get back the longest entry we can read in that time
# """
def test_get_suitable_entry():
    diary = Diary()
    entry_1 = Entry('title_1', '1 2 3')
    entry_2 = Entry('title_2', '1 2 3 4 5')
    entry_3 = Entry('title_2', '1 2 3 4 5 6 7 8 9 10')
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_3)
    assert diary.get_suitable_entry(1, 3) == entry_1
    assert diary.get_suitable_entry(1, 5) == entry_2
    assert diary.get_suitable_entry(1, 6) == entry_2
    assert diary.get_suitable_entry(1, 10) == entry_3
    assert diary.get_suitable_entry(1, 11) == entry_3