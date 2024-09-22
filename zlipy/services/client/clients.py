import asyncio

from zlipy.services.api import IAPIClient
from zlipy.services.client.interfaces import IClient


class Client(IClient):
    def __init__(self, api_client: IAPIClient) -> None:
        super().__init__()
        self.api_client = api_client

    async def run(self):
        async with self.api_client.connect() as websocket:
            while websocket.open:
                try:
                    # Read until ready event is received
                    while True:
                        response = await asyncio.wait_for(websocket.recv(), 300)
                        print(f"< Received: {response}")  # type: ignore
                        if "ReadyEvent" in response:
                            break

                        if "WaitingForConfigurationEvent" in response:
                            await websocket.send(
                                '{"event": "ConfigurationEvent", "tools": ["search"]}'
                            )

                        if "ToolCallEvent" in response:
                            await websocket.send(
                                '{"event": "ToolResponseEvent", "response": "Project folder is empty"}'
                            )

                    # Send a message to the server
                    message = input("Enter a message: ")
                    if not message:
                        await websocket.close()
                        break

                    await websocket.send(message)
                    print(f"> Sent: {message}")

                except Exception as e:
                    print(f"An error occurred: {e}")
