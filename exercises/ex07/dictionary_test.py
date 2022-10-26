"""Testing the 'dictionary' file."""

__author__ = "730598599"


from exercises.ex07.dictionary import invert, favorite_color, count

import pytest


def test_invert_keyerror() -> None:
    """Tests to ensure a KeyError is printed if a key is repeated."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_empty() -> None:
    """Tests to ensure an empty dictionary is returned if an empty dictionary is given."""
    xs: dict[str, str] = dict()
    assert invert(xs) == {}


def test_invert_many_short_strings() -> None:
    """Tests to ensure the function can return an inverted dictionary with one character strings."""
    xs: dict[str, str] = dict()
    xs["a"] = "z"
    xs["b"] = "y"
    xs["c"] = "x"
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_many_long_strings() -> None:
    """Tests to ensure the function can return an inverted dictionary with long strings."""
    xs: dict[str, str] = dict()
    xs["hello"] = "world"
    xs["computer"] = "science"
    xs["Kris"] = "Jordan"
    assert invert(xs) == {'world': 'hello', 'science': 'computer', 'Jordan': 'Kris'}


def test_favorite_color_empty() -> None:
    """Tests to ensure an empty string is returned if an empty dictionary is given."""
    xs: dict[str, str] = dict()
    assert favorite_color(xs) == ''


def test_favorite_color_most() -> None:
    """Tests to ensure the color that appears most frequently is returned."""
    xs: dict[str, str] = dict()
    xs["Marc"] = "yellow"
    xs["Ezri"] = "blue"
    xs["Kris"] = "blue"
    assert favorite_color(xs) == 'blue'


def test_favorite_color_first_most() -> None:
    """Tests to ensure that is there is a tie for most frequent color, the first color that appears is the one printed."""
    xs: dict[str, str] = dict()
    xs["Marc"] = "yellow"
    xs["Ezri"] = "blue"
    xs["Kris"] = "blue"
    xs["Anna"] = "yellow"
    xs["Jewels"] = "purple"
    assert favorite_color(xs) == 'yellow'


def test_count_empty() -> None:
    """Tests to ensure that if an empty list is given, an empty dictionary is returned."""
    xs: list[str] = list()
    assert count(xs) == {}


def test_count_ordered() -> None:
    """Tests to ensure that the function correctly counts the strings given when they are sectioned."""
    xs: list[str] = ("hello", "hello", "hello", "hola", "hola", "hi")
    assert count(xs) == {'hello': 3, 'hola': 2, 'hi': 1}


def test_count_random() -> None:
    """Tests to ensure that the function correctly counts the strings given if they are given randomly."""
    xs: list[str] = ("hello", "hola", "hello", "hi", "hola", "hello")
    assert count(xs) == {'hello': 3, 'hola': 2, 'hi': 1}
