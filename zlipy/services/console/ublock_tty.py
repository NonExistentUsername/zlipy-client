import fcntl
import os
import sys


class UnblockTTY:
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.flags_save = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        flags = self.flags_save & ~os.O_NONBLOCK
        fcntl.fcntl(self.fd, fcntl.F_SETFL, flags)

    def __exit__(self, *args):
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.flags_save)
