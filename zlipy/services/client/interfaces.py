import abc


class IClient(abc.ABC):
    @abc.abstractmethod
    async def run(self):
        pass
