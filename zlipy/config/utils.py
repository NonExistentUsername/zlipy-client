from zlipy.config.constants import DEFAULT_CONFIG_FILENAME, DEFAULT_CONFIG_TEMPLATE


def init_config():
    """Initialize the configuration."""
    with open(DEFAULT_CONFIG_FILENAME, "w+") as f:
        f.write(DEFAULT_CONFIG_TEMPLATE)
