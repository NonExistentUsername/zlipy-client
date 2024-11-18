import asyncio

from zlipy.services.client import ClientFactory
from zlipy.services.errors_handler import ErrorsHandler


def run():
    with ErrorsHandler(prefix="Error during client initialization") as handler:
        client = ClientFactory.create()

    if handler.handled_errors:
        return

    asyncio.run(client.run())
