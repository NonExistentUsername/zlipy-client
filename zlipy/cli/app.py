import asyncio

import click

from zlipy import config
from zlipy.api_client import websocket_client


@click.group()
def main():
    pass


@main.command()
def init():
    print("Init called")


@main.command()
def chat():
    asyncio.run(websocket_client(config.get_websocket_endpoint()))


cli = click.CommandCollection(sources=[main])


if __name__ == "__main__":
    cli()
