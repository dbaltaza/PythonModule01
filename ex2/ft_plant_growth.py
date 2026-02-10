"""
Exercise 2: Plant Growth
Functions that modify object attributes.
"""


class Plant:
    """A simple plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant with name, height (cm) and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def grow_plant(self, amount: int) -> None:
        """Update plant height."""
        self.height += amount

    def age_plant(self, days: int) -> None:
        """Update plant age."""
        self.age += days

    def get_info(self) -> str:
        """Return the current plant status."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_plant_growth() -> None:
    """Show how plants grow over a week."""
    plants = [
        Plant("Rose", 25, 30)]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    # Simulate a week (6 more days to reach Day 7)
    for plant in plants:
        plant.grow_plant(6)
        plant.age_plant(6)

    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
    print("Growth this week: +6cm")


if __name__ == "__main__":
    ft_plant_growth()
