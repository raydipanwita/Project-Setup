from lib.secret_diary import *
import pytest
from unittest.mock import Mock

def test_diary_is_locked_cannot_be_read():
    diary = Mock("Hi, My name is Dipa")
    secret_diary = SecretDiary(diary)
    with pytest.raises (Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"


def test_diary_is_unlocked_can_be_read_1():
    diary = Mock()
    diary.read.return_value = "Hi, My name is Dipa"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Hi, My name is Dipa"

def test_diary_is_relocked_cannot_be_read():
    diary = Mock("Hi, My name is Dipa")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises (Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"
    diary.read.assert_not_called()