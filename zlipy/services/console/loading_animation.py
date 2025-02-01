import asyncio

from rich.console import Console
from rich.progress import Progress


class LoadingAnimation:
    def __init__(self):
        self._stop_event = asyncio.Event()

    async def run(self):
        console = Console()
        progress = Progress(console=console, transient=True)
        task = progress.add_task("[cyan]Conducting analysis...", total=100)
        with Progress(transient=True) as progress:
            task = progress.add_task("Conducting analysis...", total=None)
            while not self._stop_event.is_set():
                progress.update(task, advance=0)
                await asyncio.sleep(0.0001)

        progress.stop()

    def stop(self):
        self._stop_event.set()

    async def start(self):
        self._stop_event.clear()
        await self.run()
