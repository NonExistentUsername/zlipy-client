import asyncio

import websockets

from zlipy.services.client import ClientFactory


def run():
    asyncio.run(ClientFactory.create().run())
