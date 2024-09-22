from zlipy.services.api import APIClientFactory
from zlipy.services.client.clients import Client
from zlipy.services.client.interfaces import IClient


class ClientFactory:
    @staticmethod
    def create() -> IClient:
        return Client(APIClientFactory.create())
