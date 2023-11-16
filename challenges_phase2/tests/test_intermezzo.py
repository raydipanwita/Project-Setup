from lib.intermezzo import *

def test_say_hello_for_Dipa():
    name = say_hello("Dipa")
    assert name == "hello Dipa"

def test_say_hello_for_Aditya():
    name = say_hello("Aditya")
    assert name == "hello Aditya"

def test_encode_aa():
    newcode = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert newcode == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"


def test_decode_ab():
    secondcode = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert secondcode == "theswiftfoxjumpedoverthelazydog"