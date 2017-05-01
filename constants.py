from enum import Enum

class Page(Enum):
    HOME = 1
    GAME = 2
    HISCORES = 3
    HABITS = 4
    ENTERNAME = 5
    LOGIN = 6

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    NONE = 5