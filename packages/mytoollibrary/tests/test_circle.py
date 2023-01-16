"""
Tests for circle class
"""
import math as M
import unittest
import pytest

# from ...mathtools.circle import Circle
from mathtools import Circle


class TestCircle(unittest.TestCase):
    # @patch("packages.oliverstools.activedirectory.active_directory_helper.GraphClient.get")
    def test_passing_string_to_constructor(self):

        # Arrange

        # Act
        with pytest.raises(Exception):
            _ = Circle("Abc")

        # Assert

    def test_simple_area_calculation(self):

        # Arrange
        radius = 2.0
        expected_result = radius * M.pi

        my_circle = Circle(radius)

        # Act
        result = my_circle.area()

        # Assert
        assert result == expected_result

    def test_simple_diameter_calculation(self):

        # Arrange
        radius = 2.0
        expected_result = radius * 2

        my_circle = Circle(radius)

        # Act
        result = my_circle.diameter()

        # Assert
        assert result == expected_result

    def test_simple_circumference_calculation(self):

        # Arrange
        radius = 2.0
        expected_result = radius * 2 * M.pi

        my_circle = Circle(radius)

        # Act
        result = my_circle.circumference()

        # Assert
        assert result == expected_result
