import asyncio

import rich

from zlipy.services.client import ClientFactory, IClient


def run():
    try:
        client = ClientFactory.create()
    except Exception as e:
        rich.print(f"[red]Error during client initialization: {e}[/red]")
        return

    asyncio.run(client.run())
