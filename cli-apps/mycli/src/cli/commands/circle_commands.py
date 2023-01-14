"""
Math functions, using external packages
"""

import click

from mytoollibrary.mathtools.circle import Circle


@click.group()
def circle_commands():
    """
    Methods for circles
    """


@circle_commands.command(name="area")
@click.option("--radius", "-r", required=True, help="Radius of circle")
def area(
    radius: float,
):
    """
    Calculates area of a circle
    """
    my_circle = Circle(radius=radius)
    result = my_circle.area()
    print(result)


@circle_commands.command(name="diameter")
@click.option("--radius", "-r", required=True, help="Diameter of circle")
def diameter(
    radius: float,
):
    """
    Retrieving values of a circle
    """
    my_circle = Circle(radius=radius)
    result = my_circle.diameter()
    print(result)


@circle_commands.command(name="circumference")
@click.option("--radius", "-r", required=True, help="Circumference of circle")
def circumference(
    radius: float,
):
    """
    Retrieving values of a circle
    """
    my_circle = Circle(radius=radius)
    result = my_circle.circumference()
    print(result)
