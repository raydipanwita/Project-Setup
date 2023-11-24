class ReadableEntryFinder():
    def __init__(self, diary):
        self.diary = diary

    def extract(self, wpm, min):
        entries = self.diary.all()
        if self.readable_in_time(wpm, min, entries[0]):
            return entries[0]
        else:
            return None
        
    def readable_in_time(self, wpm, min, entry):
        length_readble = wpm * min
        return self.word_count(entry.contents) <= length_readble


    def word_count(self, text):
        return len(text.split(" "))