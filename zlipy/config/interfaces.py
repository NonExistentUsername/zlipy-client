import abc


class IConfig(abc.ABC):
    @abc.abstractmethod
    @property
    def api_key(self) -> str:
        pass
