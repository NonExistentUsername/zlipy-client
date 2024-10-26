import configparser

from zlipy.config.configs import DefaultConfig
from zlipy.config.constants import DEFAULT_CONFIG_FILENAME
from zlipy.config.interfaces import IConfig


class ConfigFactory:
    @staticmethod
    def create() -> IConfig:
        filename = DEFAULT_CONFIG_FILENAME
        config = configparser.ConfigParser()
        config.read(filename)

        if "settings" not in config.sections():
            raise ValueError(
                f"[bold red]settings[/] section not found in configuration file. Please, ensure you write it correctly inf your [bold red]{DEFAULT_CONFIG_FILENAME}[/] file"
            )

        if api_key := config["settings"].get("api_key"):
            return DefaultConfig(api_key)
        else:
            raise ValueError(
                "[bold red]api_key[/] not found in configuration file. Please, ensure you write it correctly inf your [bold red]{DEFAULT_CONFIG_FILENAME}[/] file"
            )
