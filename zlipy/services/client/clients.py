import asyncio
import json

import aioconsole  # type: ignore
import websockets

from zlipy.config.interfaces import IConfig
from zlipy.domain.events import EventFactory, IEvent
from zlipy.domain.tools import ITool
from zlipy.services.api import IAPIClient
from zlipy.services.client.interfaces import IClient


class Client(IClient):
    def __init__(
        self,
        api_client: IAPIClient,
        config: IConfig,
        tools: dict[str, ITool] | None = None,
    ) -> None:
        super().__init__()
        self.api_client = api_client
        self.config = config
        self.tools: dict[str, ITool] = tools or {}

    async def _call_tool(self, tool_name: str, query: str):
        tool = self.tools.get(tool_name)

        return f"Tool {tool_name} not found" if tool is None else await tool.run(query)

    def _pretty_print_message(self, message: str):
        print(f"Message: {message}")

    async def _send_event(
        self, websocket: websockets.WebSocketClientProtocol, event: IEvent
    ):
        await websocket.send(json.dumps({"event": event.name, **event.data}))

    async def _handle_event(
        self, websocket: websockets.WebSocketClientProtocol, event: IEvent
    ):
        if event.name == "ToolCallEvent":
            await self._send_event(
                websocket,
                EventFactory.create(
                    {
                        "event": "SearchToolCallResponseEvent",
                        "documents": await self._call_tool(
                            event.data["tool"], event.data["query"]
                        ),
                    }
                ),
            )

        if event.name == "WaitingForConfigurationEvent":
            await self._send_event(
                websocket,
                EventFactory.create(
                    {"event": "ConfigurationEvent", "tools": list(self.tools.keys())}
                ),
            )

        if event.name == "AgentMessageEvent":
            self._pretty_print_message(event.data["message"])

    def _stop_handle_events_condition(self, event: IEvent) -> bool:
        return event.name == "ReadyEvent"

    async def _handle_events(self, websocket: websockets.WebSocketClientProtocol):
        while True:
            response = json.loads(await asyncio.wait_for(websocket.recv(), 300))

            print(f"< Received: {response}")

            event = EventFactory.create(response)

            if self._stop_handle_events_condition(event):
                print("< Ready event received")
                break

            await self._handle_event(websocket, event)

    async def run(self):
        async with self.api_client.connect(api_key=self.config.api_key) as websocket:
            while websocket.open:
                try:
                    # Read until ready event is received
                    await self._handle_events(websocket)

                    # Send a message to the server
                    message = await aioconsole.ainput("Enter a message: ")
                    if not message:
                        await websocket.close()
                        break

                    await websocket.send(message)
                    print(f"> Sent: {message}")

                except Exception as e:
                    import traceback

                    traceback.print_exc()
                    print(f"An error occurred: {e}")
