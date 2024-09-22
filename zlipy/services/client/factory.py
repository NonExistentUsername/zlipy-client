from zlipy.domain.tools import CodeBaseSearch, ITool
from zlipy.services.api import APIClientFactory
from zlipy.services.client.clients import Client
from zlipy.services.client.interfaces import IClient


class ClientFactory:
    @staticmethod
    def create() -> IClient:
        tools: dict[str, ITool] = {
            "search": CodeBaseSearch(),
        }

        return Client(APIClientFactory.create(), tools=tools)
