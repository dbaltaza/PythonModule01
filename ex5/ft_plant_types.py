"""
Exercise 5: Plant Types
Inheritance with specialized plant classes.
"""


class Plant:
    """A basic plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant with name, height (cm) and age (days)."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """A flower with a color."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Create a flower with a color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        """Return a blooming message."""
        return f"{self.name} is blooming beautifully!"

    def __str__(self) -> str:
        """Return flower as a string."""
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")


class Tree(Plant):
    """A tree with trunk diameter."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: float) -> None:
        """Create a tree with trunk diameter (cm)."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        """Calculate shade area from trunk size."""
        import math
        area = math.pi * (self.trunk_diameter / 2) ** 2 / 100
        return f"{self.name} provides {int(area)} square meters of shade"

    def __str__(self) -> str:
        """Return tree as a string."""
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {int(self.trunk_diameter)}cm diameter")


class Vegetable(Plant):
    """A vegetable with harvest info."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Create a vegetable with harvest season and nutritional value."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutrition(self) -> str:
        """Return nutrition info."""
        return f"{self.name} is {self.nutritional_value.lower()}"

    def __str__(self) -> str:
        """Return vegetable as a string."""
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest")


def ft_plant_types() -> None:
    """Show different plant types."""
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    print(rose)
    print(rose.bloom())
    print()

    oak = Tree("Oak", 500, 1825, 50)
    print(oak)
    print(oak.produce_shade())
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    print(tomato)
    print(tomato.nutrition())


if __name__ == "__main__":
    ft_plant_types()
