"""
Text functions
"""

import click


@click.group(name="text")
def text_commands():
    """
    Methods for text
    """


@text_commands.command(name="upper")
@click.argument("input-text")
def upper(
    input_text: str,
):
    """
    Returns text in upper casing
    """
    result = input_text.upper()
    print(result)


@text_commands.command(name="lower")
@click.argument("input-text")
def lower(
    input_text: str,
):
    """
    Returns text in upper casing
    """
    result = input_text.lower()
    print(result)
