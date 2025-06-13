# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Diary                      │
│                            │
│ - entries                  │
│ - tasks                    │
│ - contacts                 │
│ - add_entry()              │
│ - add_task()               │
│ - get_all_entries()        │
│ - get_all_tasks()          │
│ - get_entry(wpm, time)     │
│ - get_contacts             │
│   =>                       │
└───────────┬────────────────┘
            │
            │ owns lists of
            ▼
┌─────────────────────────┐
│ Entry(title, content)   │
│                         │
│ - title                 │
│ - content               │
│ - format()              │
│   => "TITLE: CONTENT"   │
└─────────────────────────┘
┌─────────────────────────┐
│ Task(task, completed)   │
│                         │
│ - description           │
│ - complete              │
│ - format()              │
│   => "DESCRIPTION"      │
└─────────────────────────┘
┌─────────────────────────┐
│ Contact(name, number)   │
│                         │
│ - name                  │
│ - number                │
│ - format()              │
│   => "NAME: NUMBER"     │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   entries: list of diary entries 
    #   tracks: list of instances of Track
    #   contacts: list of names with numbers from diary entries

    def __init__(self):
        pass # No code here yet

    def add_entry(self, title, content):
        # Parameters:
        #   title: string for title
        #   content: string for content
        # Side-effects:
        #   Creates and adds entry to list of entries
        # Returns:
        #   None
        pass # No code here yet

    def add_task(self, description):
        # Parameters:
        #   description: string describing task
        # Side-effects:
        #   Creates and adds task to list of tasks
        # Returns:
        #   None
        pass # No code here yet

    def get_entry(self, wpm, minutes):
        # Parameters:
        #   wpm: int for words per minute
        #   minutes: int for minutes available to read 
        # Side-effects:
        #   None
        # Returns:
        #   best matched entry from entries without going over 
        pass # No code here yet

    def get_all_entries(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   List of all entries
        pass # No code here yet

    def get_all_tasks(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   List of all tasks
        pass # No code here yet

    def get_all_contacts(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   List of all contacts
        pass # No code here yet


class Entry:
    # User-facing properties:
    #   title: string
    #   content: string

    def __init__(self, title='', content=''):
        # Parameters:
        #   title: string
        #   content: string
        # Side-effects:
        #   None
        # Returns:
        #   new entry
        pass # No code here yet

class Task:
    # User-facing properties:
    #   desciption: string
    #   completed: boolean

    def __init__(self, description=''):
        # Parameters:
        #   description: string
        # Side-effects:
        #   None
        # Returns:
        #   new tasks with complete set to False by default
        pass # No code here yet

class Contact:
    # User-facing properties:
    #   name: string
    #   number: string

    def __init__(self, name='', number=''):
        # Parameters:
        #   name: string
        #   number: string
        # Side-effects:
        #   None
        # Returns:
        #   new contact
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a Diary
We can add entries
And retrieve those entries
"""
diary = Diary()
entry_1 = Entry('title_1', 'content_1')
entry_2 = Entry('title_2', 'content_2')
diary.add_entry(entry_1)
diary.add_entry(entry_2)
diary.get_all_entries() # => [entry_1, entry_2]

"""
Given a Diary
We can add tasks
And retrieve those tasks
"""
diary = Diary()
task_1 = Task('description_1')
task_2 = Task('description_2')
diary.add_task(task_1)
diary.add_task(task_2)
diary.get_all_tasks() # => [task_1, task_2]

"""
Given a Diary
We can add entries with phonenumber and they will be parsed and saved
We can then retrieve any saved contact details
"""
diary = Diary()
entry_1 = Entry('title_1', 'content_1 Pete: 570-560-7834')
entry_2 = Entry('title_2', 'content_2')
diary.add_entry(entry_1)
diary.add_entry(entry_2)
diary.get_all_contacts() # => [contact_1]

"""
Given a Diary
We can add entries
We can provide a time and wpm
And get back the longest entry we can read in that time
"""
diary = Diary()
entry_1 = Entry('title_1', '1 2 3 4 5')
entry_2 = Entry('title_2', '1 2 3')
diary.add_entry(entry_1)
diary.add_entry(entry_2)
diary.get_entry(1, 3) # => entry_2


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a title and content
We can create an Entry
"""
entry = Entry("title", "content")
entry.title # => "title"
entry.content # => "content"

"""
Given a description
We can create a task
"""
task = Task("description")
task.description # => "description"
task.complete # => False

"""
Given a name and number as strings
We can create a contact
"""
contact = Contact("Pete", "570-560-7834")
contact.name # => "Pete"
contact.number # => "570-560-7834"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
