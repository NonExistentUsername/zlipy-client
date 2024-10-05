import contextlib
import os

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import DeepLake  # type: ignore
from langchain_core.embeddings import Embeddings

from zlipy.config.interfaces import IConfig
from zlipy.domain.filesfilter import FilesFilterFactory, IFilesFilter
from zlipy.domain.tools.interfaces import ITool
from zlipy.services.embeddings import APIEmbeddings


def load_docs() -> list:
    root_dir = os.getcwd()
    docs = []

    files_filter: IFilesFilter = FilesFilterFactory.create()

    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if not files_filter.ignore(os.path.join(dirpath, file)):
                with contextlib.suppress(Exception):
                    loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")
                    docs.extend(loader.load_and_split())

    return docs


def get_db_retriever(config: IConfig):
    texts = load_docs()
    db = DeepLake.from_documents(texts, APIEmbeddings(config=config), overwrite=True)

    retriever = db.as_retriever()
    retriever.search_kwargs["distance_metric"] = "cos"
    retriever.search_kwargs["fetch_k"] = 3
    retriever.search_kwargs["k"] = 3

    return db, retriever


class CodeBaseSearch(ITool):
    def __init__(self, config: IConfig) -> None:
        self.db, self.retriever = get_db_retriever(config=config)

    async def run(self, input: str) -> list[str]:
        docs = self.retriever.invoke(input)

        return [doc.page_content for doc in docs]
