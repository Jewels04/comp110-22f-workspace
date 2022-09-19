"""'list' Utility Functions Exercise."""

__author__ = 730598599


def all(int_list: list[int], given_int: int) -> bool:
    """Generates a bool value based on whether the listen ints match the given int."""
    counter: int = 0
    located: bool = False
    while counter < len(int_list):
        if int_list[counter] == given_int:
            located = True
            counter += 1
        else:
            located = False
            return located
    return located


def max(list: list[int]) -> int:
    """Given a list of ints, the function will return the largest int value in the list."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    value: int = 0
    count: int = 0
    while count < len(list):
        if value < list[count]:
            value = list[count]
        count += 1
    return value


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Given two lists, the function will return True is every index matches between the lists."""
    counting: int = 0
    equal: bool = False
    if len(list_one) != len(list_two):
        return equal
    while counting < len(list_one):
        if list_one[counting] == list_two[counting]:
            equal = True
            counting += 1
        else:
            equal = False
            return equal
    return equal