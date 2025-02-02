import rich
from httpx import HTTPStatusError

from zlipy.services.errors_handler.utils import pretty_time


class RequestErrorFormatter:
    def format(self, exc_value) -> str:
        if not isinstance(exc_value, HTTPStatusError):
            return f"{exc_value}"

        if exc_value.response is None:
            return f"{exc_value}"

        status_code = exc_value.response.status_code
        if status_code == 404:
            return "Cannot connect to the server. Please check your internet connection or try again later."
        elif status_code == 401:
            return "Unauthorized. Please check your API key."
        elif status_code == 403:
            return "Forbidden. You do not have permission to access this resource."
        elif status_code == 408:
            return "Request timeout. Please try again."
        elif status_code == 429:
            try:
                return f"Too many requests. Please slow down and try again in {pretty_time(int(exc_value.response.headers['Retry-After']))}."
            except (KeyError, ValueError):
                return "Too many requests. Please slow down and try again later."
        elif status_code == 503:
            return "Service unavailable. Please try again later."
        elif status_code >= 500 and status_code < 600:
            return "Server error. Please try again later."

        return f"{exc_value}"


class ErrorsHandler:
    def __init__(
        self,
        prefix: str | None = None,
        debug: bool = False,
    ) -> None:
        self.prefix = prefix
        self.debug = debug

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

        if self.debug:
            raise exc_value

        self._handled_errors = True

        return True
