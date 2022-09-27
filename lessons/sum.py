"""Example of writing a test subject."""


def sum(xs: list[float]) -> float:
    """Compute the sum of a list"""
    total: float = 0.0
    for item in xs:
        total += item
    return total