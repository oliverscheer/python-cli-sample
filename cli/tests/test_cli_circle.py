from click.testing import CliRunner

from ..commands.circle import area, diameter, circumference

# from jdf_cli.commands.config import list_all


def test_cli_circle_area_short_version():
    """
    circle area
    """
    test_args = ["-r", 2.0]

    runner = CliRunner()
    result = runner.invoke(area, args=test_args)
    assert result.exit_code == 0, "Command 'area' raised an error"


def test_cli_circle_area_long_version():
    """
    circle area
    """
    test_args = ["--radius", 2.0]

    runner = CliRunner()
    result = runner.invoke(area, args=test_args)
    assert result.exit_code == 0, "Command 'area' raised an error"


def test_cli_circle_area_without_args():
    """
    circle area
    """
    test_args = []

    runner = CliRunner()
    result = runner.invoke(area, args=test_args)
    assert result.exit_code == 2, "Command 'area' misses args"


def test_cli_circle_area_with_wrong_args():
    """
    circle area
    """
    test_args = ["--dummy", 1.0]

    runner = CliRunner()
    result = runner.invoke(area, args=test_args)
    assert result.exit_code == 2, "Command 'area' wrong args"


def test_cli_circle_diameter_short_version():
    """
    circle area
    """
    test_args = ["-r", 2.0]

    runner = CliRunner()
    result = runner.invoke(diameter, args=test_args)
    assert result.exit_code == 0, "Command 'diameter' raised an error"


def test_cli_circle_diameter_long_version():
    """
    circle area
    """
    test_args = ["-r", 2.0]

    runner = CliRunner()
    result = runner.invoke(diameter, args=test_args)
    assert result.exit_code == 0, "Command 'area' misses args"


def test_cli_circle_diameter_without_args():
    """
    circle area
    """
    test_args = []

    runner = CliRunner()
    result = runner.invoke(diameter, args=test_args)
    assert result.exit_code == 2, "Command 'area' misses args"


def test_cli_circle_circumference_short_version():
    """
    circle area
    """
    test_args = ["-r", 2.0]

    runner = CliRunner()
    result = runner.invoke(circumference, args=test_args)
    assert result.exit_code == 0, "Command 'circumference' raised an error"


def test_cli_circle_circumference_long_version():
    """
    circle area
    """
    test_args = ["--radius", 2.0]

    runner = CliRunner()
    result = runner.invoke(circumference, args=test_args)
    assert result.exit_code == 0, "Command 'circumference' raised an error"


def test_cli_circle_circumference_without_args():
    """
    circle area
    """
    test_args = []

    runner = CliRunner()
    result = runner.invoke(circumference, args=test_args)
    assert result.exit_code == 2, "Command 'area' misses args"
