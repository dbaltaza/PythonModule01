"""
Exercise 1: Garden Data
Working with multiple objects in a tuple.
"""


class Plant:
    """A simple plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant with name, height (cm) and age (days)."""
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    """Show info for multiple plants."""
    plants = (
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    )

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}:", f"{plant.height}cm,", f"{plant.age} days old")


if __name__ == "__main__":
    ft_garden_data()
