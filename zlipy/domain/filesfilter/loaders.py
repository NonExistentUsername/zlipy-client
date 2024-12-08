import os

from zlipy.domain.filesfilter.interfaces import IFilesFilter, IProjectStructureLoader


class DefaultProjectStructureLoader(IProjectStructureLoader):
    def __init__(self, files_filter: IFilesFilter):
        self.files_filter = files_filter

    def _load(self, dir_path: str) -> list[str | dict]:
        result: list[str | dict] = []

        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)

            if os.path.isdir(item_path):
                if sub_result := self._load(item_path):
                    result.append({item: sub_result})

            elif not self.files_filter.ignore(item_path):
                result.append(item)

        return result

    def load(self) -> list[str | dict]:
        return self._load(os.getcwd())
