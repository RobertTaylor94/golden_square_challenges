import pytest # type: ignore
from lib.present import *

def test_present_starts_empty():
    present = Present()
    assert present.contents == None

def test_wrap_updates_present_contents():
    present = Present()
    present.wrap("Minecraft")
    assert present.contents == "Minecraft"

def test_error_if_wrap_and_contents_full():
    present = Present()
    present.wrap("puppy")
    with pytest.raises(Exception) as e:
        present.wrap("kitten")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap():
    present = Present()
    present.wrap("Nanoblocks")
    result = present.unwrap()
    assert result == "Nanoblocks"

def test_error_when_unwrapping_empty_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
