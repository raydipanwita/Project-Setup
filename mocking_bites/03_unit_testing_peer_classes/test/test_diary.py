from lib.diary import *

def test_constructs_read_contents():
    diary = Diary("Hi, My name is Dipa")
    assert diary.read() == "Hi, My name is Dipa"
