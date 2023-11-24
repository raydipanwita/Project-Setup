import pytest
from lib.music_library import *
from lib.track import *

"""
When I add multiple tracks
They are refelected in the property
"""

def test_multiple_tasks_reflected_in_property():
    library = MusicLibrary()
    track1 = Track("Ed Sheeran", "Perfect")
    track2 = Track("Taylor Swift", "Romeo Juliet")
    library.add(track1)
    library.add(track2)
    assert library.tracks == [track1, track2]

"""
When I add multiple tracks
And search for a track title
I get a matching track back
"""

def test_multiple_tasks_reflected_in_property():
    library = MusicLibrary()
    track1 = Track("Ed Sheeran", "Perfect")
    track2 = Track("Taylor Swift", "Romeo Juliet")
    library.add(track1)
    library.add(track2)
    assert library.search("Ed Sheeran") == [track1]