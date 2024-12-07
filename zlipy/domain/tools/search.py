import contextlib
import os

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import DeepLake  # type: ignore
from langchain_core.embeddings import Embeddings

from zlipy.config.interfaces import IConfig
from zlipy.domain.filesfilter import FilesFilterFactory, IFilesFilter
from zlipy.domain.tools.interfaces import ITool
from zlipy.services.embeddings import APIEmbeddings


def load_docs(config: IConfig) -> list:
    root_dir = os.getcwd()
    docs = []

    files_filter: IFilesFilter = FilesFilterFactory.create(
        ignore_patterns=config.ignored_patterns
    )

    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if not files_filter.ignore(os.path.join(dirpath, file)):
                with contextlib.suppress(Exception):
                    if config.debug:
                        print(f"Loading file: {os.path.join(dirpath, file)}")

                    loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")
                    temp_docs: list = loader.load_and_split()
                    for doc in temp_docs:
                        doc.metadata["path"] = os.path.join(dirpath, file).replace(
                            root_dir, ""
                        )
                    docs.extend(temp_docs)

    return docs


def get_db_retriever(config: IConfig):
    texts = load_docs(config=config)
    db = DeepLake.from_documents(texts, APIEmbeddings(config=config), overwrite=True)

    retriever = db.as_retriever()
    retriever.search_kwargs["distance_metric"] = "cos"
    retriever.search_kwargs["fetch_k"] = 6
    retriever.search_kwargs["k"] = 6

    return db, retriever


class CodeBaseSearch(ITool):
    def __init__(self, config: IConfig) -> None:
        self.db, self.retriever = get_db_retriever(config=config)

    async def run(self, input: str) -> list[dict]:
        docs = self.retriever.invoke(input)

        return [
            {
                "path": item.metadata["path"],
                "content": item.page_content,
            }
            for item in docs
        ]
