from lib.string_builder import *

def test_starts_with_empty_string():
    builder = StringBuilder()
    assert builder.str == ''

def test_add_method_adds_to_empty_string():
    builder = StringBuilder()
    builder.add("Hello, World!")
    assert builder.str == "Hello, World!"

def test_output_returns_str():
    builder = StringBuilder()
    builder.add("Hello, John Doe!")
    result = builder.output()
    assert result == "Hello, John Doe!"

def test_size_returns_string_length_is_six():
    builder = StringBuilder()
    builder.add("Senile")
    result = builder.size()
    assert result == 6