from langchain_core.embeddings import Embeddings

from zlipy.config.interfaces import IConfig
from zlipy.services.api.factory import APIClientFactory
from zlipy.services.api.interfaces import IAPIClient


class APIEmbeddings(Embeddings):
    def __init__(self, config: IConfig) -> None:
        super().__init__()

        self.client: IAPIClient = APIClientFactory.create()
        self.config: IConfig = config

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        import asyncio

        return asyncio.run(self.aembed_documents(texts))

    def embed_query(self, text: str) -> list[float]:
        import asyncio

        return asyncio.run(self.aembed_query(text))

    async def aembed_documents(self, texts: list[str]) -> list[list[float]]:
        return await self.client.generate_embeddings(
            api_key=self.config.api_key, inputs=texts
        )

    async def aembed_query(self, text: str) -> list[float]:
        return (await self.client.generate_embeddings(self.config.api_key, [text]))[0]
