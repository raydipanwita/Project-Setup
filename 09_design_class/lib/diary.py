class Diary:
    def __init__(self):
        self.list_of_entries = []
    
    def add(self, entry):
        self.list_of_entries.append(entry)
        
    def all(self):
        return self.list_of_entries
