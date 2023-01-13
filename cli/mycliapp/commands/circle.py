# """
# Math functions, using external packages
# """

# import click

# from oliverstools.mathtools.circle import Circle


# @click.group()
# def circle():
#     """
#     Methods for circles
#     """


# @circle.command(name="area"Q)
# @click.option("--radius", "-r", required=True, help="Radius of circle")
# def area(
#     radius: float,
# ):
#     """
#     Calculates area of a circle
#     """
#     c1 = Circle(radius=radius)
#     print(c1.area())


# @circle.command(name="diameter")
# @click.option("--radius", "-r", required=True, help="Diameter of circle")
# def diameter(
#     radius: float,
# ):
#     """
#     Retrieving values of a circle
#     """
#     circle_result = Circle(radius=radius)
#     print(circle_result.diameter())


# @circle.command(name="circumference")
# @click.option("--radius", "-r", required=True, help="Circumference of circle")
# def circumference(
#     radius: float,
# ):
#     """
#     Retrieving values of a circle
#     """
#     circle_result = Circle(radius=radius)
#     print(circle_result.circumference())
