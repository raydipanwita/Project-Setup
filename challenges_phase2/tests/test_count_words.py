from lib.count_words import *

def test_count_words_one():
    string = count_words("hello")
    assert string == 1

def test_count_words_multiple():
    string = count_words("hello I am Dipa")
    assert string == 4