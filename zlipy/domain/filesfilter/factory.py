from zlipy.domain.filesfilter.constants import GITIGNORE_FILENAME, FilesFilterTypes
from zlipy.domain.filesfilter.filters import (
    AllowedExtensionsFilesFilter,
    GitIgnoreFilesFilter,
    MergeFilesFilter,
)
from zlipy.domain.filesfilter.interfaces import IFilesFilter


class FilesFilterFactory:
    @staticmethod
    def create(
        files_filter_type: FilesFilterTypes = FilesFilterTypes.DEFAULT,
    ) -> IFilesFilter:
        if files_filter_type == FilesFilterTypes.DEFAULT:
            return MergeFilesFilter(
                GitIgnoreFilesFilter(GITIGNORE_FILENAME),
                AllowedExtensionsFilesFilter(),
            )

        if files_filter_type == FilesFilterTypes.GITIGNORE:
            return GitIgnoreFilesFilter(GITIGNORE_FILENAME)

        if files_filter_type == FilesFilterTypes.ALLOWED_EXTENSIONS:
            return AllowedExtensionsFilesFilter()

        raise ValueError(f"Unknown files filter type: {files_filter_type}")
