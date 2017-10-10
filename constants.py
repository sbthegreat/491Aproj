from enum import Enum
from enum import IntEnum

class Page(Enum):
    HOME = 1
    GAME = 2
    HISCORE = 3
    HABITS = 4
    ENTERNAME = 5
    CALIBRATE = 6
    CONFIRM = 7

class Direction(IntEnum): # numbers are set so that -enum value swaps direction
    UP = 1
    RIGHT = 2
    DOWN = -1
    LEFT = -2
    NONE = 0

class Quadrant(IntEnum):
    TOPRIGHT = 270
    TOPLEFT = 180
    BOTTOMLEFT = 90
    BOTTOMRIGHT = 0
    
TRAIL_COLOR = (255,0,0) # the BGR color of the trail following the tracked object during gameplay
FPS = 60 # the FPS the game runs at
POINT_LIMIT = 5; # the maximum number of points stored
MIN_SWIPE = 130 # the minimum number of pixels the distance a swipe has to move before it is registered
COOLDOWN = 0.5 # the number of seconds swipes are not tracked after a swipe occurs
MIN_SIZE = 10000 # the smallest size a collection of thresholded pixels can be to register as a tracked object

UP_NAV = (300,100) # where to place text that indicates to user how to navigate
DOWN_NAV = (300,600)
RIGHT_NAV = (700, 300)
LEFT_NAV = (0, 300)

# the HSV color values that are tracked
LOW_H = 54
HIGH_H = 82
LOW_S = 77
HIGH_S = 138
LOW_V = 42
HIGH_V = 128

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA_SIZE = 26

GAME_INCREMENT = 30 # how many pixels each swipes moves the game screen during calibration
GAME_SIZE = 150 # how many pixels the radius of the game screen circle is
GAME_LENGTH = 8 # how many seconds each game lasts for
SECTION_LENGTH = 2

GERM_COLORS = [(0,255,255),(0,128,255),(0,255,0)]
GERM_SPEEDS = [4, 3, 2]
GERM_SIZES = [10, 15, 20]
