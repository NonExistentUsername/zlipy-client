import abc


class IFilesFilter(abc.ABC):
    @abc.abstractmethod
    def ignore(self, relative_path: str) -> bool:
        pass


class IProjectStructureLoader(abc.ABC):
    @abc.abstractmethod
    def load(self) -> dict[str, list[str | dict]]:
        pass
