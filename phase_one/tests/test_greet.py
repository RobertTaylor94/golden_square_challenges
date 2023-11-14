from lib.greet import *

def test_greet_returns_name():
    result = greet('Sheila')
    assert result == "Hello, Sheila!"