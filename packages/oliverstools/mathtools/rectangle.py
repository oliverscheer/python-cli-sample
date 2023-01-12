"""
Rectangle definition and methods
"""


class Rectangle:
    """
    Rectangle class for math calculations
    """

    def __init__(self, a, b) -> None:
        self.length_a = a
        self.length_b = b

    def __str__(self) -> str:
        output = (
            "Rectangle("
            f"a={str(self.length_a)}, "
            f"b={str(self.length_b)}, "
            f"area={str(self.area())}, "
            f"circumference={str(self.circumference())})"
        )
        return output

    def area(self):
        """
        Calculate area of cirlce
        """
        area = self.length_a * self.length_b

        return area

    def circumference(self):
        """
        Calculate circumference of cirlce
        """
        circumference = 2 * (self.length_a * self.length_b)
        return circumference
