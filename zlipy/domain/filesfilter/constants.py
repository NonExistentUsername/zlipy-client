import enum

GITIGNORE_FILENAME = ".gitignore"


class FilesFilterTypes(enum.IntEnum):
    DEFAULT = enum.auto()

    GITIGNORE = enum.auto()
    ALLOWED_EXTENSIONS = enum.auto()
