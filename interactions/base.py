# Normal libraries
from typing import ClassVar

__version__ = "4.0.0"
__repo_url__ = "https://github.com/discord-py-interactions/discord-py-interactions"


class Data:
    """An object representing constants for the library."""

    LOGGER: ClassVar[str] = "interactions.log"


class Route:
    """An object representing different URL routing paths."""

    API: ClassVar[str] = "https://discord.com/api/v9"
    GATEWAY: ClassVar[str] = "wss://gateway.discord.gg/?v=9"
