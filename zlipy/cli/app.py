import warnings

from langchain.globals import set_debug, set_verbose

warnings.filterwarnings("ignore")

import click

from zlipy.api_client import run
from zlipy.config import init_config


@click.group()
def main():
    pass


@main.command()
def init():
    """Initialize the configuration."""
    init_config()
    click.echo("Configuration initialized.")


@main.command()
def chat():
    """Start a chat."""
    run()


cli = click.CommandCollection(sources=[main])


if __name__ == "__main__":
    cli()
