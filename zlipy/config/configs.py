from zlipy.config.interfaces import IConfig


class DefaultConfig(IConfig):
    def __init__(self, api_key: str) -> None:
        super().__init__()
        self._api_key = api_key

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def debug(self) -> bool:
        return False
