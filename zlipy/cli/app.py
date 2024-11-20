import warnings

warnings.filterwarnings("ignore")

import click

from zlipy.api_client import run
from zlipy.config import init_config
from zlipy.config.factory import ConfigFactory


@click.group()
def main():
    pass


@main.command()
def init():
    """Initialize the configuration."""
    init_config()
    click.echo("Configuration initialized.")


@main.command()
@click.option(
    "--disable-markdown-formatting",
    "-dmf",
    is_flag=True,
    help="Disable markdown formatting in the console.",
)
@click.option(
    "--debug",
    "-d",
    is_flag=True,
    help="Enable debug mode (more verbose output).",
)
def chat(disable_markdown_formatting: bool, debug: bool):
    """Start a chat."""
    run(
        config=ConfigFactory.create(
            debug=debug,
            disable_markdown_formatting=disable_markdown_formatting,
        )
    )


cli = click.CommandCollection(sources=[main])


if __name__ == "__main__":
    cli()
