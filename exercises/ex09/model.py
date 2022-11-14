"""The model classes maintain the state and logic of the simulation."""


from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt

__author__ = "730598599"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Calculates the distance between two cells."""
        how_far: float = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return how_far


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        
    def tick(self) -> None:
        """Reassign an object's location attribute."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "red"
        if self.is_immune():
            return "dark magenta"

    def contract_disease(self) -> None:
        """Assigns the INFECTED constant to the sickness attribute of a cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Determines whether a cell is vulnerable."""
        vulnerable: bool = True
        if self.sickness == constants.VULNERABLE:
            return vulnerable
        else:
            vulnerable = False
            return vulnerable

    def is_infected(self) -> bool:
        """Determines if a cell is infected."""
        sick: bool = True
        if self.sickness >= constants.INFECTED:
            return sick
        else:
            sick = False
            return sick

    def contact_with(self, other: Cell) -> None:
        """Determines whether an infected cell comes into contact with a vulnerable cell."""
        if self.is_infected() is True and other.is_vulnerable() is True:
            other.contract_disease()
        elif self.is_vulnerable() is True and other.is_infected() is True:
            self.contract_disease()

    def immunize(self) -> None:
        """Assigns the IMMUNE constant to the sickness attribute of a cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Determines if a cell is immune."""
        immunity: bool = True
        if self.sickness == constants.IMMUNE:
            return immunity


class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0:
            raise ValueError("Some number of cell objects must begin infected.")
        if immune >= cells:
            raise ValueError("Improper number of immune cells.")
        for _ in range(cells - (infected + immune)):
            start_location_pop: Point = self.random_location()
            start_direction_pop: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location_pop, start_direction_pop)
            self.population.append(cell)
        for _ in range(infected):
            start_location_infected: Point = self.random_location()
            start_direction_infected: Point = self.random_direction(speed)
            cell_infected: Cell = Cell(start_location_infected, start_direction_infected)
            cell_infected.contract_disease()
            self.population.append(cell_infected)
        for _ in range(immune):
            start_location_immune: Point = self.random_location()
            start_direction_immune: Point = self.random_direction(speed)
            cell_immune: Cell = Cell(start_location_immune, start_direction_immune)
            cell_immune.immunize()
            self.population.append(cell_immune)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks whether two cells come into contact."""
        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False