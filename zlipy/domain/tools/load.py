import contextlib
import os

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import DeepLake  # type: ignore
from langchain_core.embeddings import Embeddings

from zlipy.config.interfaces import IConfig
from zlipy.domain.filesfilter import FilesFilterFactory, IFilesFilter
from zlipy.domain.tools.interfaces import ITool
from zlipy.services.console import aprint
from zlipy.services.embeddings import APIEmbeddings


class LoadFileTool(ITool):
    async def _pretty_print_message(self, message: str):
        await aprint(message)

    async def run(self, input: str) -> str | None:
        relative_path = input
        root_dir = os.path.abspath(os.getcwd())

        await self._pretty_print_message(f"Root dir: {root_dir}")
        await self._pretty_print_message(f"Relative path: {relative_path}")

        full_path = os.path.join(
            root_dir,
            relative_path[1:] if relative_path.startswith("/") else relative_path,
        )

        await self._pretty_print_message(f"Loading file: {full_path}")

        if not os.path.exists(full_path):
            return None

        with open(full_path, "r") as file:
            return file.read()
