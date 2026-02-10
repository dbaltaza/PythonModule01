"""
Exercise 3: Plant Factory
Creating multiple objects and counting them.
"""


class Plant:
    """A simple plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant with name, height (cm) and age (days)."""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    """Create several plants and show them."""
    plants = (
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    )

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print("\nTotal plants created:", len(plants))


if __name__ == "__main__":
    ft_plant_factory()
