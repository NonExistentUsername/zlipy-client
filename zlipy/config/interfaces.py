import abc


class IConfig(abc.ABC):
    @property
    @abc.abstractmethod
    def api_key(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def debug(self) -> bool:
        pass
