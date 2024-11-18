import asyncio
import json

import aioconsole  # type: ignore
import rich
import websockets
from rich.markdown import Markdown

from zlipy.config.interfaces import IConfig
from zlipy.domain.events import EventFactory, IEvent
from zlipy.domain.tools import ITool
from zlipy.services.api import IAPIClient
from zlipy.services.client.interfaces import IClient
from zlipy.services.console import aprint
from zlipy.services.console.loading_animation import LoadingAnimation


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
        self.loading_animation = LoadingAnimation()

    async def _call_tool(self, tool_name: str, query: str):
        tool = self.tools.get(tool_name)

        return f"Tool {tool_name} not found" if tool is None else await tool.run(query)

    async def _pretty_print_message(self, message: str):
        await aprint(Markdown(f"{message}"))

    async def _debug_print(self, object):
        if self.config.debug:
            await aprint(object)

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
            await self._pretty_print_message(event.data["message"])

    def _stop_handle_events_condition(self, event: IEvent) -> bool:
        return event.name == "ReadyEvent"

    def _stop_animation_events_condition(self, event: IEvent) -> bool:
        return event.name in ["ReadyEvent", "AgentMessageEvent"]

    async def _handle_events(self, websocket: websockets.WebSocketClientProtocol):
        while True:
            for _ in range(3):
                try:
                    response = json.loads(
                        await asyncio.wait_for(websocket.recv(), timeout=300)
                    )
                    break
                except Exception as e:
                    await aioconsole.aprint(f"Error: {e}")
                    continue

            await self._debug_print(f"< Received: {response}")

            event = EventFactory.create(response)

            if self._stop_animation_events_condition(event):
                self.loading_animation.stop()
                await asyncio.sleep(0.0005)  # Await for the animation to stop

            if self._stop_handle_events_condition(event):
                await self._debug_print("< Ready event received")
                break

            await self._handle_event(websocket, event)

    async def run(self):
        async with self.api_client.connect(api_key=self.config.api_key) as websocket:
            while websocket.open:
                try:
                    # Read until ready event is received with loading animation
                    # await self._handle_events(websocket)
                    await asyncio.gather(
                        self.loading_animation.start(), self._handle_events(websocket)
                    )

                    message = await aioconsole.ainput("Enter a message: ")

                    if not message:
                        await websocket.close()
                        break

                    await websocket.send(message)

                    await self._debug_print(f"> Sent: {message}")

                except Exception as e:
                    import traceback

                    await aioconsole.aprint(traceback.format_exc())
