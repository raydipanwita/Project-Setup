from lib.diary import *
from lib.diary_entry import *
from lib.phonenumberextractor import *

"""
When I add multiple diary entries
And i call Phonenosextract
i get list of phone nos from all diary entries
"""
def test_extracts_phone_number():
    diary = Diary()
    entry1 = Diary_entry("Title 1" , "My friend 07000000000 and  07000000001")
    entry2 = Diary_entry("Title 2" , "My Contents 07000000002")
    diary.add(entry1)
    diary.add(entry2)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == ["07000000000", "07000000001", "07000000002"]


"""
When I add no diary entries, 
And I call Phone NosExtractor
It returns None
"""

# diary = Diary()
# extractor = PhoneNumberyExtractor(diary)
# extractor.extract() == []
