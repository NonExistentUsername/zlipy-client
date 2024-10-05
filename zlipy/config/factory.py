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
            raise ValueError("settings section not found in configuration file")

        if api_key := config["settings"].get("api_key"):
            return DefaultConfig(api_key)
        else:
            raise ValueError("api_key not found in configuration file")
