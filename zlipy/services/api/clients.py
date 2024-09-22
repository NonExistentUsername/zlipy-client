import httpx
import websockets

from zlipy.services.api.constants import API_BASE
from zlipy.services.api.interfaces import IAPIClient


class APIClient(IAPIClient):
    def __init__(self, base: str = API_BASE):
        super().__init__()
        self.base = base
        self.ws_base = base.replace("https", "ws").replace("http", "ws")

    async def generate_embeddings(self, texts: list[str]) -> list[list[float]]:
        endpoint = f"{self.base}/tools/embeddings/"

        async with httpx.AsyncClient() as client:
            response = await client.post(endpoint, json={"texts": texts})
            response.raise_for_status()

            return response.json()

    def connect(self):
        endpoint = f"{self.ws_base}/ws/"
        return websockets.connect(endpoint, ping_timeout=60, ping_interval=10)
