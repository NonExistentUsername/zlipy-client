from datetime import datetime, timedelta, timezone


def pretty_time(seconds: int) -> str:
    return str(timedelta(seconds=seconds))
