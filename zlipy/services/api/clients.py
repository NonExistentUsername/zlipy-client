import httpx
import websockets

from zlipy.services.api.constants import API_BASE
from zlipy.services.api.interfaces import IAPIClient


class APIClient(IAPIClient):
    def __init__(self, base: str = API_BASE):
        super().__init__()
        self.base = base
        self.ws_base = base.replace("https", "wss").replace("http", "ws")

    async def generate_embeddings(
        self, api_key: str, inputs: list[str]
    ) -> list[list[float]]:
        endpoint = f"{self.base}/tools/embeddings/?token={api_key}"

        async with httpx.AsyncClient() as client:
            response = await client.post(endpoint, json={"texts": inputs}, timeout=60)
            response.raise_for_status()

            return response.json()

    def connect(self, api_key: str) -> websockets.connect:
        endpoint = f"{self.ws_base}/ws/?token={api_key}"
        return websockets.connect(endpoint, ping_timeout=500, ping_interval=10)
