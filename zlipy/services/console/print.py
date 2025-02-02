from rich.console import Console

from zlipy.services.console.ublock_tty import UnblockTTY


async def aprint(*args, **kwargs):
    with UnblockTTY():
        console = Console()
        console.print(*args, **kwargs)


async def asimple_print(*args, **kwargs):
    with UnblockTTY():
        print(*args, **kwargs)
