from Validator import *
from Engine import *
from Dictionary import *
import pytest

# Testujemy tą funkcję ponieważ jest ona jedną z najważniejszych w naszym programie i bez niej nie mógł by on działać
@pytest.mark.parametrize("test_input,expected", [("kot", True), ("jajo", False), ("patyk", True)])
def test_Validator(test_input, expected):
    assert Validator.Izogram(test_input) == expected

# Testujemy tą funkcję aby przypadkiem nie wprowadzić błędów do naszego pliku co uniemożliwiło by grę
@pytest.mark.parametrize("test_input,expected", [("kot", False), ("lod", True), ("patyk", False)])
def test_Sprawdz_czy_jest(test_input, expected):
    assert Dictionary.Sprawdz_czy_jest(test_input) == expected

# Testy tej funkcji są powiązane z poprzednimi i wykonujemy je w tym samym celu
@pytest.mark.parametrize("test_input, expected", [("mikolaj", 0), ("jez", 0), ("kot", 0)])
def test_Dodawanie_slow(test_input,expected):
    assert Dictionary.Dodawanie_slow(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(1, ([3,4])), (2, ([5,6])), (3, ([7,50]))])
def test_Zmiana_poziomu(test_input,expected):
    assert Maszyna.Zmiana_poziomu(test_input) == expected