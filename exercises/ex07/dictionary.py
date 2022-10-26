"""Dictionary Functions Assignment."""

__author__ = "730598599"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given list and returns the inverted list."""
    reverse: dict[str, str] = dict()
    for key in input:
        if input[key] in reverse:
            raise KeyError("Repeated key.")
        reverse[input[key]] = key
    return reverse


def favorite_color(favs: dict[str, str]) -> str:
    """Returns the most frequently appearing color."""
    tracker: list[str] = list()
    color: str = ""
    other: dict[str, int] = dict()
    number: int = 0
    for key in favs:
        tracker.append(favs[key])
    other = count(tracker)
    for key in other:
        if other[key] > number:
            number = other[key]
            color = key
    return color
    

def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a string is present in a list."""
    result: dict[str, int] = dict()
    counter: int = 0
    while counter < len(values):
        if values[counter] in result:
            result[values[counter]] += 1
        else:
            result[values[counter]] = 1
        counter += 1
    return result
