import abc
from dataclasses import dataclass


class ITool(abc.ABC):
    @abc.abstractmethod
    async def run(self, input: str):
        pass
