import abc
from typing import Coroutine

import websockets


class IAPIClient(abc.ABC):
    @abc.abstractmethod
    async def generate_embeddings(
        self, api_key: str, inputs: list[str]
    ) -> list[list[float]]:
        pass

    @abc.abstractmethod
    def connect(
        self,
        api_key: str,
    ) -> websockets.connect:
        pass
