from zlipy.config.factory import ConfigFactory
from zlipy.domain.tools import CodeBaseSearch, ITool
from zlipy.services.api import APIClientFactory
from zlipy.services.client.clients import Client
from zlipy.services.client.interfaces import IClient


class ClientFactory:
    @staticmethod
    def create() -> IClient:
        config = ConfigFactory.create()

        tools: dict[str, ITool] = {
            "search": CodeBaseSearch(config=config),
        }

        return Client(APIClientFactory.create(), config=config, tools=tools)
