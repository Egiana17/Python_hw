import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" hello world", "hello world"),
    ("   python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("privet ", "privet "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("skypro", "s", True),
    ("hello world", "o", True),
    ("python", "p", True),
])
def test_contains_positive(input_str, symbol_str, expected):
    assert string_utils.contains(input_str, symbol_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("SkyPro", "a", False),
    ("", "7", False),
    ("privet ", "z", False),
])
def test_contains_negative(input_str, symbol_str, expected):
    assert string_utils.contains(input_str, symbol_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("skypro", "s", "kypro"),
    ("hello world", "o", "hell wrld"),
    ("python", "p", "ython"),
])
def test_delete_symbol_positive(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("SkyPro", "a", "SkyPro"),
    ("", "7", ""),
    ("privet ", "z", "privet "),
])
def test_delete_symbol_negative(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected
