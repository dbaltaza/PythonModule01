"""
Exercise 0: Garden Introduction
Basic class and object creation.
"""


class Plant:
    """A simple plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant with name, height (cm) and age (days)."""
        self.name = name
        self.height = height
        self.age = age


def ft_garden_intro() -> None:
    """Show basic plant info."""
    plant = Plant("Rose", 25, 30)

    print("== Welcome to my Garden ==")
    print("Name:", plant.name)
    print("Height:", f"{plant.height}cm")
    print("Age:", plant.age, "days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
