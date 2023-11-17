import pytest
from lib.single_class import *

def test_errors_for_empty_string_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    assert str(e.value) == "Diary entry must not be empty"


# class TestDiaryEntry():
def test_diary_entry_one():
    word = DiaryEntry("My Diary", "This is my first entry")
    result = word.format()
    assert result ==  "My Diary: This is my first entry"

def test_count_words():
    word = DiaryEntry("My Diary", "This is my first entry")
    result = word.count_words()
    assert result == 7

def test_reading_time_for_two_words():
    word = DiaryEntry("My Diary", "This is")
    result = word.reading_time(2)
    assert result == 1


def test_reading_time_for_five_words():
    word = DiaryEntry("My Diary", "This is my first entry")
    result = word.reading_time(2)
    assert result == 3


def test_reading_chunks_for_five_words():
    word = DiaryEntry("My Diary", "This is my first entry")
    result = word.reading_chunk(2, 1)
    assert result == "This is"


def test_reading_chunks_called_twice():
    word = DiaryEntry("My Diary", "This is my first entry in")
    assert word.reading_chunk(2, 2) == "This is my first"
    assert word.reading_chunk(2, 2) == "entry in"
    assert word.reading_chunk(2, 2) == "This is my first"


def test_reading_chunks_called_with_exact_ending():
    word = DiaryEntry("My Diary", "This is my first entry in")
    assert word.reading_chunk(2, 2) == "This is my first"
    assert word.reading_chunk(2, 1) == "entry in"
    assert word.reading_chunk(2, 2) == "This is my first"