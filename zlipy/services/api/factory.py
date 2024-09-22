from zlipy.services.api.clients import APIClient
from zlipy.services.api.interfaces import IAPIClient


class APIClientFactory:
    @staticmethod
    def create() -> IAPIClient:
        return APIClient()
