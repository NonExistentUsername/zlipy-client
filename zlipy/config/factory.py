import configparser

from zlipy.config.configs import DefaultConfig
from zlipy.config.constants import DEFAULT_CONFIG_FILENAME
from zlipy.config.interfaces import IConfig


class ConfigFactory:
    @staticmethod
    def create(
        debug: bool = False,
        deep_dive: bool = False,
        disable_markdown_formatting: bool = False,
    ) -> IConfig:
        filename = DEFAULT_CONFIG_FILENAME
        config = configparser.ConfigParser()
        config.read(filename)

        if "settings" not in config.sections():
            raise ValueError(
                f"[bold red]settings[/] section not found in configuration file. Please, ensure you write it correctly inf your [bold red]{DEFAULT_CONFIG_FILENAME}[/] file"
            )

        if api_key := config["settings"].get("api_key"):
            ignored_patterns = []

            for pattern in config["settings"].get("ignored_patterns", "").split(","):
                if pattern_stripped := pattern.strip():
                    ignored_patterns.append(pattern_stripped)

            return DefaultConfig(
                api_key=api_key,
                debug=debug,
                deep_dive=deep_dive,
                disable_markdown_formatting=disable_markdown_formatting,
                ignored_patterns=ignored_patterns,
            )
        else:
            raise ValueError(
                "[bold red]api_key[/] not found in configuration file. Please, ensure you write it correctly inf your [bold red]{DEFAULT_CONFIG_FILENAME}[/] file"
            )
