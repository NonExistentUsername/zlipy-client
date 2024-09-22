from zlipy.config.constants import DEFAULT_CONFIG_FILENAME


def init_config():
    """Initialize the configuration."""
    with open(DEFAULT_CONFIG_FILENAME, "w+") as f:
        f.write("""\n""")
