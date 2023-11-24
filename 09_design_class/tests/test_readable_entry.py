from lib.readable_entry_extractor import *
from lib.diary import *
from lib.diary_entry import *

"""
When I one diary entry
And I call readble EntryExtractor@extract
With wpm of 2 and min of 2 
It gets that diary entry
"""
def test_one_diary_entry_to_call():
    diary = Diary()
    entry1 = Diary_entry("Title 1" , "One Two Three Four")
    diary.add(entry1)
    extractor = ReadableEntryFinder(diary)
    assert extractor.extract(wpm = 2, min =2) == entry1

"""
When I add multiple entries, one readble
And I call readble EntryExtractor"extract
With wpm of 2 and min of 2 
It gets the readble diary entry
"""
def test_returns_none_if_entries_dont_fit_time():
    diary = Diary()
    entry1 = Diary_entry("Title 1" , "One Two Three Four Five")
    entry2 = Diary_entry("Title 2" , "One Two Three Four ive Six")
    diary.add(entry1)
    diary.add(entry2)
    extractor = ReadableEntryFinder(diary)
    assert extractor.extract(wpm = 2, min =2) == None


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

