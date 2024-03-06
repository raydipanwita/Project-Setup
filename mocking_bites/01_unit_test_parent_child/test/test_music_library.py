from lib.music_library import *
from unittest.mock import Mock

"""
When I add multiple tracks
And search for a keyword
I get a tracks matching that keyword
"""

def test_search_by_keyword():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)    
    assert library.search("hello") == [fake_matching]

"""
Initially, tracks is empty
"""
def test_track_empty():
    library = MusicLibrary()
    assert library.tracks == []

"""
When I add multiple tracks
They show in list of tracks
"""
def test_track_updated_with_new_tracks():
    library = MusicLibrary()
    track1 = Mock()
    track2 = Mock()
    library.add(track1)
    library.add(track2)
    assert library.tracks == [track1, track2]

