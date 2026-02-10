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

    def grow_plant(self, amount: int) -> None:
        """Update plant height."""
        self.height += amount

    def age_plant(self, days: int) -> None:
        """Update plant age."""
        self.age += days

    def get_info(self) -> str:
        """Return the current plant status."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


def ft_plant_factory() -> None:
    """Create several plants and show them."""
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = [Plant(*data) for data in plant_data]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.get_info()}")
    print("Total plants created:", len(plants))


if __name__ == "__main__":
    ft_plant_factory()
