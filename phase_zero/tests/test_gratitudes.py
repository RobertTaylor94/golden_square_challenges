from lib.gratitudes import *

def test_initialise_gratitudes_with_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_add_one_gratitude_to_list():
    gratitudes = Gratitudes()
    gratitudes.add("Gravy")
    assert gratitudes.gratitudes == ["Gravy"]

def test_add_multiple_gratitudes_to_list():
    gratitudes = Gratitudes()
    gratitudes.add("Pizza")
    gratitudes.add("Family")
    gratitudes.add("Water")
    assert gratitudes.gratitudes == ["Pizza", "Family", "Water"]

def test_format():
    gratitudes = Gratitudes()
    gratitudes.add("Pizza")
    gratitudes.add("Family")
    gratitudes.add("Water")
    result = gratitudes.format()
    assert result == "Be grateful for: Pizza, Family, Water"