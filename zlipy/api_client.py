import asyncio

import websockets


async def websocket_client(uri):
    async with websockets.connect(uri, ping_timeout=60, ping_interval=10) as websocket:
        while websocket.open:
            try:
                # Read until ready event is received
                while True:
                    response = await asyncio.wait_for(websocket.recv(), 300)
                    print(f"< Received: {response}")
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


if __name__ == "__main__":
    uri = "ws://localhost:8000/ws/"  # The WebSocket endpoint
    asyncio.run(websocket_client(uri))
