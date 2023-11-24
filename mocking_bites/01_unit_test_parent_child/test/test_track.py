from lib.track import *
from unittest.mock import Mock

"""
Given a title and an artist
And a search keyword for the full title
matches is true
"""

def test_matches_on_full_title():
    track = Track("Cat", "Dog")
    assert track.matches("Cat") == True

"""
Given a title and an artist
And a search keyword for the partial title
matches is true
"""

def test_matches_on_partial_title():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Cat") == True


"""
Given a title and an artist
And a search keyword for the full artist
matches is true
"""

def test_matches_on_full_artist():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Dog Artist") == True


"""
Given a title and an artist
And a search keyword for the partial title
matches is true
"""

def test_matches_on_partial_artist():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Dog") == True


"""
Given a title and an artist
And a search keyword that does not match wither
matches is False
"""

def test_matches_on_keyword_not_in_title_or_artist():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Zebra") == False
