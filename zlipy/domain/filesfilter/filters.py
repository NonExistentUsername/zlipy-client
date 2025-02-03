import os
import re
from re import Pattern
from typing import Callable, List

from gitignore_parser import parse_gitignore  # type: ignore
from gitignore_parser import IgnoreRule, handle_negation, rule_from_pattern

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
             ".css",  # CSS files
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
             ".sql",  # SQL script files
             ".log",  # Log files
             ".env",  # Environment files
             ".ts",   # TypeScript files
             ".jsx",  # JSX files
             ".htmlx",# HTMLX files
             ".tsx",  # TypeScript JSX files
             ".vue",  # Vue.js files
             ".scss", # SASS files
             ".sass", # SASS files
             ".tf",   # Terraform files
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


class IgnoredFilesFilter(IFilesFilter):
    def __init__(self, patterns: List[str]):
        """Initialize the filter with a list of .gitignore-like patterns."""
        self.patterns = patterns
        # self.rules: List[IgnoreRule] = self._convert_patterns_to_regex(patterns)
        self.matches = self._convert_patterns_to_match_func(patterns)

    def _convert_patterns_to_match_func(
        self, patterns: List[str]
    ) -> Callable[[str], bool]:
        rules = []
        for pattern in patterns:
            rule = rule_from_pattern(pattern, base_path=".")
            rules.append(rule)

        if not any(r.negation for r in rules):
            return lambda file_path: any(r.match(file_path) for r in rules)
        else:
            # We have negation rules. We can't use a simple "any" to evaluate them.
            # Later rules override earlier rules.
            return lambda file_path: handle_negation(file_path, rules)

    def ignore(self, relative_path: str) -> bool:
        """Check if the relative path matches any of the ignored patterns."""
        return self.matches(relative_path)
