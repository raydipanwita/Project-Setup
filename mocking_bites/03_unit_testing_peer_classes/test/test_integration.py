from lib.secret_diary import *
from lib.diary import *
from unittest.mock import Mock
import pytest

def test_read_diary():
    diary = Diary("Hi, My name is Dipa")
    assert diary.read() == "Hi, My name is Dipa"


def test_diary_is_locked_cannot_be_read():
    diary = Diary("Hi, My name is Dipa")
    secret_diary = SecretDiary(diary)
    with pytest.raises (Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"

def test_diary_is_unlocked_can_be_read():
    diary = Diary("Hi, My name is Dipa")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Hi, My name is Dipa"


def test_diary_is_relocked_cannot_be_read_returns_nothing():
    diary = Diary("Hi, My name is Dipa")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises (Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"