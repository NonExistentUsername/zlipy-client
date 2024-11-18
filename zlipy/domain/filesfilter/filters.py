import os
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


class AllowedExtensionsFilesFilter(IFilesFilter):
    def __init__(self) -> None:
        super().__init__()

        # fmt: off
        self._allowed_extensions = {
             ".py",   # Python files
             ".txt",  # Text files
             ".md",   # Markdown files
             ".json", # JSON files
             ".csv",  # Comma-separated values
             ".xml",  # XML files
             ".html", # HTML files
             ".ini",  # INI configuration files
             ".yaml", ".yml",  # YAML files
             ".java", # Java source files
             ".js",   # JavaScript files
             ".c",    # C source files
             ".cpp",  # C++ source files
             ".h",    # Header files
             ".hpp",  # C++ header files
             ".rb",   # Ruby files
             ".php",  # PHP files
             ".go",   # Go source files
             ".rs",   # Rust source files
             ".kt",   # Kotlin source files
             ".sh",   # Shell script files
             ".sql"   # SQL script files
             ".log"   # Log files
             ".env"   # Environment files
        }
        # fmt: on

    def ignore(self, relative_path: str) -> bool:
        _, extenstion = os.path.splitext(relative_path)
        return extenstion not in self._allowed_extensions


class MergeFilesFilter(IFilesFilter):
    def __init__(self, *args: IFilesFilter) -> None:
        super().__init__()

        self._filters = args

    def ignore(self, relative_path: str) -> bool:
        return any(filter.ignore(relative_path) for filter in self._filters)
