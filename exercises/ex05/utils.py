"""Building list utility functions and testing them."""

___author___ = "730598599"


def only_evens(xs: list[int]) -> list[int]:
    """Returns only the even integers in a given list."""
    counter: int = 0
    even_list: list[int] = list()
    while counter < len(xs):
        if xs[counter] % 2 == 0:
            even_list.append(xs[counter])
        counter += 1
    return even_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Generates a list that combined the tow given lists."""
    new_list: list[int] = list_one + list_two
    return new_list


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a subset list of a given list based on the specified start index and one less of the end index."""
    new_list: list[int] = list()
    counter: int = start_index
    if start_index < 0:
        counter = 0
    if end_index > len(a_list):
        end_index = len(a_list)
    while counter < end_index:
        new_list.append(a_list[counter])
        counter += 1
    return new_list