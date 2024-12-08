from zlipy.config.interfaces import IConfig
from zlipy.domain.tools import CodeBaseSearch, ITool, LoadFileTool
from zlipy.services.api import APIClientFactory
from zlipy.services.client.clients import Client
from zlipy.services.client.interfaces import IClient


class ClientFactory:
    @staticmethod
    def create(config: IConfig) -> IClient:
        tools: dict[str, ITool] = {
            "search": CodeBaseSearch(config=config),
            "load": LoadFileTool(),
        }

        return Client(APIClientFactory.create(), config=config, tools=tools)
