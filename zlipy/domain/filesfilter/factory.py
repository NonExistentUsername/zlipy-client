from zlipy.domain.filesfilter.constants import GITIGNORE_FILENAME, FilesFilterTypes
from zlipy.domain.filesfilter.filters import GitIgnoreFilesFilter
from zlipy.domain.filesfilter.interfaces import IFilesFilter


class FilesFilterFactory:
    @staticmethod
    def create(
        files_filter_type: FilesFilterTypes = FilesFilterTypes.GITIGNORE,
    ) -> IFilesFilter:
        if files_filter_type == FilesFilterTypes.GITIGNORE:
            return GitIgnoreFilesFilter(GITIGNORE_FILENAME)

        raise ValueError(f"Unknown files filter type: {files_filter_type}")
