# """
# Math functions, using external packages
# """

# import click

# from oliverstools.mathtools import Rectangle


# @click.group()
# def rect():
#     """
#     Methods for rectangles
#     """


# @rect.command(name="area")
# @click.option("--length-a", "-a", required=True, help="Lenght of side a")
# @click.option("--length-b", "-b", required=True, help="Lenght of side b")
# def area(
#     length_a: float,
#     length_b: float,
# ):
#     """
#     Calculate area of a rectangle
#     """
#     rectangle = Rectangle(a=length_a, b=length_b)
#     print(rectangle.area())


# @rect.command(name="circumference")
# @click.option("--length-a", "-a", required=True, help="Lenght of side a")
# @click.option("--length-b", "-b", required=True, help="Lenght of side b")
# def circumference(
#     length_a: float,
#     length_b: float,
# ):
#     """
#     Calculate circumference of a rectangle
#     """
#     rectangle = Rectangle(a=length_a, b=length_b)
#     print(rectangle.circumference())
