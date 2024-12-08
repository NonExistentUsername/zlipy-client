import asyncio

from zlipy.config.interfaces import IConfig
from zlipy.services.client import ClientFactory
from zlipy.services.errors_handler import ErrorsHandler


def run(config: IConfig) -> None:
    with ErrorsHandler(
        prefix="Error during client initialization",
        debug=config.debug,
    ) as handler:
        client = ClientFactory.create(config=config)

    if handler.handled_errors:
        return

    asyncio.run(client.run())
