class Plant:
    """
    Basic plant class that other plant types inherit from.

    Attributes:
        name (str): The plant's name
        height (int): The plant's height in cm
        age (int): The plant's age in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days"

    def grow(self) -> None:
        """Increase the plant's height and age by 1."""
        self.height += 1
        self.age += 1


class Flower(Plant):
    """
    A flowering plant that inherits from Plant.

    Attributes:
        color (str): The color of the flower
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display a message that the flower is blooming."""
        print(f"{self.name} is blooming beautifully!\n")

    def __str__(self) -> str:
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"


class Tree(Plant):
    """
    A tree that inherits from Plant.

    Attributes:
        trunk_diameter (int): The diameter of the tree trunk in cm
    """

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Display the area of shade produced by the tree."""
        shade_area = self.trunk_diameter * self.height // 100
        print(f"{self.name} provides {shade_area} square meters of shade\n")

    def __str__(self) -> str:
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    A vegetable plant that inherits from Plant.

    Attributes:
        harvest_season (str): The season when the vegetable is harvested
        nutritional_value (str): The main nutritional value of the vegetable
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest(self) -> None:
        """Display the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}\n")

    def __str__(self) -> str:
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
                f"{self.harvest_season} harvest")


def ft_plant_types() -> None:
    """
    Demonstrate different plant types and their behaviors.
    """
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 1000, 30)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 15, 120, "fall", "vitamin A")

    print(rose)
    rose.bloom()
    print(tulip)
    tulip.bloom()

    print(oak)
    oak.produce_shade()
    print(pine)
    pine.produce_shade()

    print(tomato)
    tomato.harvest()
    print(carrot)
    carrot.harvest()


if __name__ == "__main__":
    ft_plant_types()