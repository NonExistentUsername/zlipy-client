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

    @property
    @abc.abstractmethod
    def disable_markdown_formatting(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def ignored_patterns(self) -> list[str]:
        pass

    @property
    @abc.abstractmethod
    def deep_dive(self) -> bool:
        pass
