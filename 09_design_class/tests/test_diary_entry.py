from lib.diary_entry import *


def test_diary_entry():
    entry = Diary_entry("Title 1" , "Contents 1")
    assert entry.title == "Title 1"
    assert entry.contents == "Contents 1"

# def test_for_viewing():
#     entry = Diary_entry("Title 1" , "Contents 1")
#     assert entry.title == "Title 1"
#     assert entry.contents == "Contents 1"