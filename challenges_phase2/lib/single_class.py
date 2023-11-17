import math
class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception ("Diary entry must not be empty")
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"    

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        word_in_contents = len(self.contents.split())
        return math.ceil(word_in_contents / wpm)

    def reading_chunk(self, wpm, minutes):
        
        words_user_can_read = wpm * minutes
        words = self.contents.split()

        if self.read_so_far >= len(words):
            self.read_so_far = 0

        chunk_starts = self.read_so_far 
        chunk_ends = self.read_so_far + words_user_can_read
        chunk_words = words[chunk_starts:chunk_ends]
        self.read_so_far = chunk_ends
        return " ".join(chunk_words)
