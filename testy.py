from Dictionary import *
from Engine import *
import pytest

@pytest.mark.parametrize("test_input,expected", [("kot", True), ("jajo", False), ("patyk", True)])
def test_Validator(test_input, expected):
    assert Validator.Izogram(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("kot", False), ("lod", True), ("patyk", False)])
def test_Sprawdz_czy_jest(test_input, expected):
    assert Dictionary.Sprawdz_czy_jest(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("pies", 0), ("lodowy", 0), ("patyk", 0)])
def test_Dodawanie_slow(test_input, expected):
    assert Dictionary.Dodawanie_slow(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(1, [3,4]), (2, [5,6]), (3, [7,50])])
def test_Zmiana_poziomu(test_input, expected):
    assert Maszyna.Zmiana_poziomu(test_input) == expected

