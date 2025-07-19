from enum import Enum 


class Artemis_Color(Enum):
    RED = "\033[1;49;31m"
    END_LINE = "\033[0m"
    GREEN = "\033[1;32m"
    WHITE = "\033[1m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;49;34m"
    DASH_WHITE_BACKGROUND = "\033[1;47m"
    DASH_WHITE_BACKGROUND_END = "\033[0m"