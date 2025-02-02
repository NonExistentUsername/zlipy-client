import warnings

warnings.filterwarnings("ignore")

import click

from zlipy.api_client import run
from zlipy.config import init_config
from zlipy.config.factory import ConfigFactory


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if not ctx.invoked_subcommand:
        run(
            config=ConfigFactory.create(
                debug=False,
                boost=False,
                disable_markdown_formatting=False,
            )
        )


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
    default=False,
)
@click.option(
    "--debug",
    "-d",
    is_flag=True,
    help="Enable debug mode (more verbose output).",
    default=False,
)
@click.option(
    "--deep-dive",
    "-dd",
    is_flag=True,
    help="Enable deep dive mode (advanced analysis).",
    default=False,
)
def chat(disable_markdown_formatting: bool, debug: bool, deep_dive: bool):
    """Start a chat."""
    run(
        config=ConfigFactory.create(
            debug=debug,
            deep_dive=deep_dive,
            disable_markdown_formatting=disable_markdown_formatting,
        )
    )


cli = main


if __name__ == "__main__":
    cli()
