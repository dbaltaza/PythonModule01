"""
Exercise 4: Garden Security
Using private attributes and getters/setters.
"""


class SecurePlant:
    """A plant with protected data."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a secure plant with validation."""
        self._name = name
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set height if it's valid (not negative)."""
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        """Get the plant height."""
        return self._height

    def set_age(self, age: int) -> None:
        """Set age if it's valid (not negative)."""
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        """Get the plant age."""
        return self._age

    def get_name(self) -> str:
        """Get the plant name."""
        return self._name

    def __str__(self) -> str:
        """Return plant as a string."""
        return f"{self._name} ({self._height}cm, {self._age} days)"


def ft_garden_security() -> None:
    """Show how validation works."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant}")


if __name__ == "__main__":
    ft_garden_security()
