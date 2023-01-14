"""
Main of the cli
"""
import click


from .commands import text_commands, circle_commands


@click.group(help="My CLI tool")
def cli():
    """
    Entrypoint
    """


cli.add_command(circle_commands)
# cli.add_command(rect)
cli.add_command(text_commands)


def another_function():
    print("Hello, World!")


def main():
    cli()


if __name__ == "__main__":
    main()
