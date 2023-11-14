from lib.counter import *

def test_start_count_is_zero():
    counter = Counter()
    assert counter.count == 0

def test_zero_add_nine_equals_nine():
    counter = Counter()
    counter.add(9)
    assert counter.count == 9

def test_report_method():
    counter = Counter()
    counter.add(23)
    result = counter.report()
    assert result == 'Counted to 23 so far.'