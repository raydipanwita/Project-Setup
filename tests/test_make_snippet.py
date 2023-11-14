from lib.diary import *

def test_make_snippet_for_words_empty_word():
    result = make_snippet("")
    assert result == ""


def test_make_snippet_for_words_less_than_5():
    result = make_snippet("hello my name is ")
    assert result == "hello my name is "


def test_make_snippet_for_words_5():
    result = make_snippet("hello my name is dipa")
    assert result == "hello my name is dipa"

def test_make_snippet_for_words_more_than_5():
    result = make_snippet("hello my name is dipa and")
    assert result == "hello my name is dipa..."
