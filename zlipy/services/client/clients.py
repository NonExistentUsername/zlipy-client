import asyncio
import json

import websockets

from zlipy.domain.events import EventFactory, IEvent
from zlipy.services.api import IAPIClient
from zlipy.services.client.interfaces import IClient


class Client(IClient):
    def __init__(self, api_client: IAPIClient) -> None:
        super().__init__()
        self.api_client = api_client

    async def _handle_event(
        self, websocket: websockets.WebSocketClientProtocol, event: IEvent
    ):
        if event.name == "ToolCallEvent":
            await websocket.send(
                '{"event": "ToolResponseEvent", "response": "Project folder is empty"}'
            )

        if event.name == "WaitingForConfigurationEvent":
            await websocket.send('{"event": "ConfigurationEvent", "tools": ["search"]}')

    def _stop_handle_events_condition(self, event: IEvent) -> bool:
        return event.name == "ReadyEvent"

    async def _handle_events(self, websocket: websockets.WebSocketClientProtocol):
        while True:
            response = json.loads(await asyncio.wait_for(websocket.recv(), 300))

            print(f"< Received: {response}")

            event = EventFactory.create(response)

            if self._stop_handle_events_condition(event):
                break

            await self._handle_event(websocket, event)

    async def run(self):
        async with self.api_client.connect() as websocket:
            while websocket.open:
                try:
                    # Read until ready event is received
                    await self._handle_events(websocket)

                    # Send a message to the server
                    message = input("Enter a message: ")
                    if not message:
                        await websocket.close()
                        break

                    await websocket.send(message)
                    print(f"> Sent: {message}")

                except Exception as e:
                    print(f"An error occurred: {e}")
