import re

class PhoneNumberExtractor:
    def __init__(self, diary):
        self.diary = diary


    def extract(self):
        phone_number = []
        for entry in self.diary.all():
            contents = entry.contents
            print(contents)
            phone_number += re.findall(r"0[0-9]{10}", contents)
        return phone_number