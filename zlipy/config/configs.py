from zlipy.config.interfaces import IConfig


class DefaultConfig(IConfig):
    def __init__(
        self,
        api_key: str,
        debug: bool = False,
        deep_dive: bool = False,
        disable_markdown_formatting: bool = False,
        ignored_patterns: list[str] | None = None,
    ) -> None:
        super().__init__()
        self._api_key = api_key
        self._debug = debug
        self._deep_dive = deep_dive
        self._disable_markdown_formatting = disable_markdown_formatting
        self._ignored_patterns = ignored_patterns or []

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def debug(self) -> bool:
        return self._debug

    @property
    def disable_markdown_formatting(self) -> bool:
        return self._disable_markdown_formatting

    @property
    def ignored_patterns(self) -> list[str]:
        return self._ignored_patterns

    @property
    def deep_dive(self) -> bool:
        return self._deep_dive
