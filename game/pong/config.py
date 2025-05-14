from configparser import ConfigParser

config = ConfigParser()

config.read("./config.cfg")

_default_config_section = config["DEFAULT"]

WINDOW_WIDTH = int(_default_config_section.get("WindowWidth") or "1280")
WINDOW_HEIGHT = int(_default_config_section.get("WindowHeight") or "720")

_paddle_config_section = config["PADDLE"]
PADDLE_SPEED = int(_paddle_config_section.get("Speed") or "200")
