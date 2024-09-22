import abc
from typing import Coroutine

import websockets


class IAPIClient(abc.ABC):
    @abc.abstractmethod
    async def generate_embeddings(self, inputs: list[str]) -> list[list[float]]:
        pass

    @abc.abstractmethod
    def connect(
        self,
    ) -> websockets.connect:
        pass
