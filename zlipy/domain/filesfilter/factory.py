from zlipy.domain.filesfilter.constants import GITIGNORE_FILENAME, FilesFilterTypes
from zlipy.domain.filesfilter.filters import (
    AllowedExtensionsFilesFilter,
    GitIgnoreFilesFilter,
    IgnoredFilesFilter,
    MergeFilesFilter,
)
from zlipy.domain.filesfilter.interfaces import IFilesFilter, IProjectStructureLoader
from zlipy.domain.filesfilter.loaders import DefaultProjectStructureLoader


class FilesFilterFactory:
    @staticmethod
    def create(
        files_filter_type: FilesFilterTypes = FilesFilterTypes.DEFAULT,
        ignore_patterns: list[str] | None = None,
    ) -> IFilesFilter:
        if files_filter_type == FilesFilterTypes.DEFAULT:
            if not ignore_patterns:
                ignore_patterns = [
                    "deeplake/",
                    "zlipy.ini",
                    "*.log",
                    "*.sql",
                    "*.json",
                    "*.csv",
                    "*.xml",
                    "*.txt",
                ]

            return MergeFilesFilter(
                GitIgnoreFilesFilter(GITIGNORE_FILENAME),
                AllowedExtensionsFilesFilter(),
                IgnoredFilesFilter(patterns=ignore_patterns),
            )

        if files_filter_type == FilesFilterTypes.GITIGNORE:
            return GitIgnoreFilesFilter(GITIGNORE_FILENAME)

        if files_filter_type == FilesFilterTypes.ALLOWED_EXTENSIONS:
            return AllowedExtensionsFilesFilter()

        raise ValueError(f"Unknown files filter type: {files_filter_type}")


class ProjectStructureLoaderFactory:
    @staticmethod
    def create(files_filter: IFilesFilter) -> IProjectStructureLoader:
        return DefaultProjectStructureLoader(files_filter)
