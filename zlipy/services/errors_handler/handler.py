import rich
from httpx import HTTPStatusError


class RequestErrorFormatter:
    def format(self, exc_value) -> str:
        if not isinstance(exc_value, HTTPStatusError):
            return f"{exc_value}"

        if exc_value.response is None:
            return f"{exc_value}"

        if exc_value.response.status_code == 404:
            return "Cannot connect to the server. Please check your internet connection or try again later."

        if exc_value.response.status_code == 401:
            return "Unauthorized. Please check your API key."

        return f"{exc_value}"


class ErrorsHandler:
    def __init__(self, prefix: str | None = None):
        self.prefix = prefix

        self.request_error_formatter = RequestErrorFormatter()

        self._handled_errors = False

    @property
    def handled_errors(self) -> bool:
        return self._handled_errors

    def __bool__(self) -> bool:
        return self.handled_errors

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            return False

        if isinstance(exc_value, HTTPStatusError):
            formatted_value = self.request_error_formatter.format(exc_value)
        else:
            formatted_value = f"{exc_value}"

        formatted_prefix = f"{self.prefix}: " if self.prefix else ""
        final_message = f"[red]{formatted_prefix}{formatted_value}[/red]"

        rich.print(final_message)

        self._handled_errors = True

        return True
