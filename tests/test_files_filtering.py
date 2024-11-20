import pytest  # type: ignore

from zlipy.domain.filesfilter import IgnoredFilesFilter


@pytest.fixture
def ignored_files_filter():
    ignored_patterns = [
        ".git/",  # ignore everything in .git directory
        "node_modules/",  # ignore everything in node_modules directory
        "*.log",  # ignore log files
        "*.tmp",  # ignore temporary files
        "temp/*",  # ignore everything in temp directory
        "!important.log",  # do not ignore important.log
        "docs/**",  # ignore everything in docs directory and subdirectories
        "images/*.png",  # ignore all .png files in images directory
        "!images/keep.png",  # do not ignore keep.png in images directory
        "temp/**/tempfile.tmp",  # ignore tempfile.tmp in any subdirectory of temp
    ]
    return IgnoredFilesFilter(ignored_patterns)


def test_edge_case_directory_ignore(ignored_files_filter: IgnoredFilesFilter):
    assert ignored_files_filter.ignore(".git/README.md") is True
    assert ignored_files_filter.ignore("node_modules/package.json") is True
    assert ignored_files_filter.ignore("docs/file.txt") is True
    assert ignored_files_filter.ignore("docs/subdir/anotherfile.txt") is True


def test_edge_case_file_ignore(ignored_files_filter: IgnoredFilesFilter):
    assert ignored_files_filter.ignore("error.log") is True
    assert ignored_files_filter.ignore("temp/tempfile.tmp") is True
    assert ignored_files_filter.ignore("images/picture.png") is True
    assert ignored_files_filter.ignore("images/keep.png") is False  # Should not ignore


def test_edge_case_negation(ignored_files_filter: IgnoredFilesFilter):
    assert ignored_files_filter.ignore("important.log") is False  # Should not ignore
    assert ignored_files_filter.ignore("images/some_other.png") is True  # Should ignore
    assert (
        ignored_files_filter.ignore("temp/subdir/tempfile.tmp") is True
    )  # Should ignore


def test_edge_case_non_matching(ignored_files_filter: IgnoredFilesFilter):
    assert ignored_files_filter.ignore("src/main.py") is False
    assert ignored_files_filter.ignore("README.md") is False
    assert ignored_files_filter.ignore("temp/anotherfile.txt") is True


def test_edge_case_empty_patterns():
    empty_filter = IgnoredFilesFilter([])
    assert empty_filter.ignore("anyfile.py") is False  # Should not ignore anything
