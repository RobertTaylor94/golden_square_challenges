from lib.check_codeword import *

def test_correct_codeword_is_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_correct_first_last_letter():
    result = check_codeword('hare')
    assert result == 'Close, but nope.'

def test_wrong_codeword():
    result = check_codeword('otters')
    assert result == 'WRONG!'