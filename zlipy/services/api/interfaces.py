import abc


class IAPIClient(abc.ABC):
    @abc.abstractmethod
    async def generate_embeddings(self, inputs: list[str]) -> list[list[float]]:
        pass
