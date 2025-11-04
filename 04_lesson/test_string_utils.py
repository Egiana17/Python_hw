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
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "s"),
    ("hello world", "o"),
    ("python", "p"),
])
def test_contains_positive(input_str, expected):
    assert string_utils.contains(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("SkyPro", "a"),
    ("123", "7"),
    ("privet ", "z"),
])
def test_contains_negative(input_str, expected):
    assert string_utils.contains(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "s"),
    ("hello world", "o"),
    ("python", "p"),
])
def test_delete_symbol_positive(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("SkyPro", "a"),
    ("123", "7"),
    ("privet ", "z"),
])
def test_delete_symbol_negative(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected
