"""
Main of the cli
"""
import click


from .commands import circle, rect, text


@click.group(help="Olivers CLI tool")
def cli():
    """
    Entrypoint
    """


cli.add_command(circle)
cli.add_command(rect)

# cli.add_command(text)


if __name__ == "__main__":
    cli()
