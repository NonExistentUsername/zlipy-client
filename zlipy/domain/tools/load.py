import os

from zlipy.domain.tools.interfaces import ITool


class LoadFileTool(ITool):
    async def run(self, input: str) -> str | None:
        relative_path = input
        root_dir = os.path.abspath(os.getcwd())

        full_path = os.path.join(
            root_dir,
            relative_path[1:] if relative_path.startswith("/") else relative_path,
        )

        if not os.path.exists(full_path):
            return None

        with open(full_path, "r") as file:
            return file.read()
