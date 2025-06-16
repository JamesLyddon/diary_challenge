import re
from lib.entry import Entry
from lib.task import Task
from lib.contact import Contact

class Diary:
    def __init__(self):
        self.entries = []
        self.tasks = []
        self.contacts = []

    def add_entry(self, entry):
        self.extract_contact(entry)
        self.entries.append(entry)

    def add_task(self, task):
        self.tasks.append(task)

    def extract_contact(self, entry):
        matches = re.findall(r"(?:\b([A-Z][a-z]+):\s(\d{3}-\d{3}-\d{4}))|(?:call\s([A-Z][a-z]+)\s(\d{11}))"
, entry.content)
        for match in matches:
        # Each match is a tuple of 4, but only 2 fields will be non-None
            name = match[0] or match[2]
            number = match[1] or match[3]
            self.contacts.append({'name': name, 'number': number})

    def get_all_entries(self):
        return self.entries
    
    def get_all_tasks(self):
        return self.tasks
    
    def get_all_contacts(self):
        return self.contacts
    
    def get_suitable_entry(self, wpm, mins):
        best_fit = None
        current_longest = 0
        max_words = wpm * mins
        for entry in self.entries:
            length = len(entry.content.split())
            if current_longest < length <= max_words:
                current_longest = length
                best_fit = entry
        return best_fit