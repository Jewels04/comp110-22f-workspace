"""Dictionary related utility functions."""

__author__ = "730598599"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a table with only a specific numbers of rows of data."""
    result: dict[str, list[str]] = {}
    for item in table:
        values: list[int] = []
        counter: int = 0
        if len(table[item]) < rows:
            values = table[item]
        else:
            while counter < rows:
                values.append(table[item][counter])
                counter += 1
        result[item] = values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a table with only a specific subset of data."""
    result: dict[str, list[str]] = {}
    for item in names:
        result[item] = table[item]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a table with two tables combined."""
    result: dict[str, list[str]] = {}
    for item in table_one:
        result[item] = table_one[item]
    for value in table_two:
        if value in result:
            counter: int = 0
            while counter < len(table_two[value]):    
                result[value].append(table_two[value][counter])
                counter += 1
        else:
            result[value] = table_two[value]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in data."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result