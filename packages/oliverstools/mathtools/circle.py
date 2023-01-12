"""
Circle definition and methods
"""
import math as M


class Circle:
    """
    Circle class for math calculations
    """

    # radius: float = 1.0

    def __init__(self, radius: float) -> None:
        self.radius: float = float(radius)

    def __str__(self) -> str:
        output = (
            "Circle("
            f"radius={str(self.radius)}, "
            f"area={str(self.area())}, "
            f"circumference={str(self.circumference())}, "
            f"diameter={str(self.diameter())})"
        )
        return output

    def area(self):
        """
        Calculate area of cirlce
        """
        area = self.radius * M.pi

        return area

    def diameter(self):
        """
        Calculate diameter of cirlce
        """
        diameter = self.radius * 2
        return diameter

    def circumference(self):
        """
        Calculate circumference of cirlce
        """
        circumference = 2 * M.pi * self.radius
        return circumference
