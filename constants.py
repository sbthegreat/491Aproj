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

TRAIL_COLOR = (255,0,0) # the BGR color of the trail following the tracked object
FPS = 60 # the FPS the game runs at
POINT_LIMIT = FPS / 4; # the maximum number of points stored
JITTER_POINT = 1 # the pixel difference needed to actually draw a new line segment (I'm not sure if this really works as-is)
MIN_SWIPE = 50 # the minimum number of pixels the distance a swipe has to move before it is registered
COOLDOWN = 1 # the number of seconds swipes are not tracked after a swipe occurs
MIN_SIZE = 10000 # the smallest size a collection of thresholded pixels can be to be registered as a tracked object

# the HSV color values that are tracked
LOW_H = 0
HIGH_H = 40
LOW_S = 61
HIGH_S = 114
LOW_V = 103
HIGH_V = 166
# screen size should be a constant