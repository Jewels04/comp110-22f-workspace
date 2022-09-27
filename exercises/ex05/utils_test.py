"""Testing the 'utils' file."""

__author__ = "730598599"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Tests to make sure an empty list is returned if an empty list is given."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_return_many_items() -> None:
    """Tests to make sure multiple even ints are returned if multiple are given within the given list."""
    xs: list[int] = [2, 7, 6, 3, 4]
    assert only_evens(xs) == [2, 6, 4]


def test_only_evens_return_none() -> None:
    """Tests to make sure an empty list is returned if no evens ints are within the given list."""
    xs: list[int] = [1, 13, 7, 9, 55]
    assert only_evens(xs) == []


def test_concat_empty() -> None:
    """Tests to make sure an empty list is returned is two empty lists are given."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_concat_counting_ints() -> None:
    """Tests to make sure the correct list is returned when the lists have numbers counting up by 1."""
    list_one: list[int] = [1, 2, 3, 4, 5]
    list_two: list[int] = [6, 7, 8, 9, 10]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_random_ints() -> None:
    """Tests to make sure the correct list is returned when random ints are within the given lists."""
    list_one: list[int] = [2, 5, 66, 27]
    list_two: list[int] = [46, 9, 72, 3]
    assert concat(list_one, list_two) == [2, 5, 66, 27, 46, 9, 72, 3]


def test_sub_empty() -> None:
    """Tests to make sure an empty list is returned if an empty list is given."""
    a_list: list[int] = []
    start_index: int = 1
    end_index: int = 5
    assert sub(a_list, start_index, end_index) == []


def test_sub_negative_start() -> None:
    """Tests to make sure the list begins with the first index of the given list if the start index is negative."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start_index: int = -3
    end_index: int = 4
    assert sub(a_list, start_index, end_index) == [1, 2, 3, 4]


def test_sub_greater_end_than_length() -> None:
    """Tests to make sure the list ends with the last index of the given list if the end index is greater than the length of the given list."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start_index: int = 1
    end_index: int = 9
    assert sub(a_list, start_index, end_index) == [2, 3, 4, 5]