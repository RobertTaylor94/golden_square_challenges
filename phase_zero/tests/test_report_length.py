from lib.report_length import *

def test_string_length_is_six():
    result = report_length('pickle')
    assert result == "This string was 6 characters long."