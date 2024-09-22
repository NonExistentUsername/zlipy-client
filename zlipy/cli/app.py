import asyncio

import click

from zlipy.api_client import websocket_client
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
    asyncio.run(websocket_client("ws://localhost:8000/ws/"))


cli = click.CommandCollection(sources=[main])


if __name__ == "__main__":
    cli()
