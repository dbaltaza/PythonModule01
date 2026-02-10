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


def grow(height: int, days: int) -> int:
    """Calculate new height after growing for some days."""
    return height + days


def age(current_age: int, days: int) -> int:
    """Calculate new age after some days pass."""
    return current_age + days


def ft_plant_growth() -> None:
    """Show how a plant grows over a week."""
    plant = Plant("Rose", 25, 30)
    days = 1

    print(f"=== Day {days} ===")
    print(f"{plant.name}:", f"{plant.height}cm,", f"{plant.age} days old")

    while days < 6:
        days += 1

    print(f"=== Day {days + 1} ===")
    print(
        f"{plant.name}: {grow(plant.height, days)}cm, "
        f"{age(plant.age, days)} days old"
    )
    print(f"Growth this week: +{days}cm")


if __name__ == "__main__":
    ft_plant_growth()
