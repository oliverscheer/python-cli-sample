"""
Main of the cli
"""
import click


# from .commands.rect import rect
# from .commands.circle import circle
# from .commands import text_commands
from .commands.text_commands import text_commands


@click.group(help="My CLI tool")
def cli():
    """
    Entrypoint
    """


# cli.add_command(circle)
# cli.add_command(rect)
cli.add_command(text_commands)


def another_function():
    print("Hello, World!")


def main():
    cli()


if __name__ == "__main__":
    main()
