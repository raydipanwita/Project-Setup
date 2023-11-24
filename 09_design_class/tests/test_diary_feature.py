from lib.diary import *
from lib.diary_entry import *


# """
# Intially, diary has no entries
# """
# def test_for_adding_in_diary():
#     diary = Diary()
#     entry1 = Diary_entry("Title 1" , "Contents 1")
#     entry2 = Diary_entry("Title 2" , "Contents 2")
#     diary.add(entry1)
#     diary.add(entry2)
#     assert diary.all() == [entry1, entry2]


"""
Test for adding to diary:
"""

def test_for_adding_in_diary():
    diary = Diary()
    entry1 = Diary_entry("Title 1" , "Contents 1")
    entry2 = Diary_entry("Title 2" , "Contents 2")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]


"""
When I add multiple diary entries
And i call Phonenosextract
i get list of phone nos from all diary entries
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "My friend   0700000000 and  0700000001")
# entry2 = Diary_entry("Title 2" , "My Contents 0700000002")
# diary.add(entry1)
# diary.add(entry2)
# extraxtor = Phonenumberextractor(diary)
# extractor.extract() == [07000000000, 0700000001, 0700000002]


"""
When I add no diary entries, 
And I call Phone NosExtractor
It returns None
"""

# diary = Diary()
# extractor = PhoneNumberyExtractor(diary)
# extractor.extract() == []

"""
When I one multiple entries
And I call readble EntryExtractor"extract
With wpm of 2 and min of 2 
It gets that diary entry
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "One Two Three Four")
# diary.add(entry1)
# extractor = ReadbleEntryExtractor(diary)
# extractor.extract(wpm = 2, min =2) == [entry1 ]

"""
When I add multiple entries, one readble
And I call readble EntryExtractor"extract
With wpm of 2 and min of 2 
It gets the readble diary entry
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "One Two Three Four Five")
# entry2 = Diary_entry("Title 2" , "One Two Three Four")
# diary.add(entry1)
# diary.add(entry2)
# extractor = ReadbleEntryExtractor(diary)
# extractor.extract(wpm = 2, min =2) == [entry2 ]


"""
When I add multiple entries, one readble
And I call readble EntryExtractor"extract
With wpm of 2 and min of 2 
It gets the longest readble diary entry
"""

# diary = Diary()
# entry1 = Diary_entry("Title 1" , "One Two Three Four Five")
# entry2 = Diary_entry("Title 2" , "One Two Three")
# entry2 = Diary_entry("Title 2" , "One Two Three Four")
# diary.add(entry1)
# diary.add(entry2)
# diary.add(entry3)
# extractor = ReadbleEntryExtractor(diary)
# extractor.extract(wpm = 2, min =2) == [entry3 ]


"""
When I add no diary entries, 
And I call Readable EntryExtractor
It returns None
"""

# diary = Diary()
# extractor = ReadbleEntryExtractor(diary)
# extractor.extract(wpm = 2, min =2) == [entry3 ]



## 4. Create Examples as Unit Tests


# Diary

# # def test_for_adding_in_diary():
#     diary = Diary()
#     assert diary.all() == []

# # DiaryEntry

# # def test_for_adding_in_diaryentry():
# entry = DiaryEntry("Title 1" , "Contents 1")
# entry.title = "Title 1"
# entry.contents = "Contents 1"