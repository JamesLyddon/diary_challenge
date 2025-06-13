from lib.entry import Entry
from lib.task import Task
from lib.contact import Contact

class Diary:
    def __init__(self):
        self.entries = []
        self.tasks = []
        self.contacts = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_all_entries(self):
        return self.entries