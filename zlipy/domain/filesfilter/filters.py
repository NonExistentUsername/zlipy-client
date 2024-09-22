from typing import Any, Coroutine

from gitignore_parser import parse_gitignore  # type: ignore

from zlipy.domain.filesfilter.constants import GITIGNORE_FILENAME, FilesFilterTypes
from zlipy.domain.filesfilter.interfaces import IFilesFilter


class GitIgnoreFilesFilter(IFilesFilter):
    def __init__(self, filename):
        self.filename = filename
        self._matches_func = self._load__matches_func()

    def _load__matches_func(self):
        try:
            matches = parse_gitignore(".gitignore")
        except Exception:
            matches = lambda x: False

        return matches

    def ignore(self, relative_path: str) -> bool:
        return self._matches_func(relative_path)
