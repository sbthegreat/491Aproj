import numpy as np
import cv2
import collections
import time
import math
import threading
import homeController
import gameController
from enum import Enum
import constants

BG_COLOR = 0 # the background color of the game
TRAIL_COLOR = (255,0,0) # the BGR color of the trail following the tracked object
FPS = 60 # the FPS the game runs at
POINT_LIMIT = FPS / 4;
JITTER_POINT = 1 # the pixel difference needed to actually draw a new line segment (I'm not sure if this really works as-is)
MIN_SWIPE = 50 # the minimum number of pixels the distance a swipe has to move before it is registered
COOLDOWN = 1 # the number of seconds swipes are not tracked after a swipe occurs
X = 0
Y = 1

class SystemState():
    def __init__(self):
        self.trailPoints = collections.deque()
        self.currentPage = constants.Page.HOME
        self.direction = constants.Direction.NONE 
        self.removedPoint = (0,0)
        self.lastSwipe = 0
        
    def setPage(self, newPage):
        self.currentPage = newPage
    
    def resetDirection(self):
        self.direction = constants.Direction.NONE

    # adds points to the trail, pops off oldest point if past length limit and returns it
    def addPoint(self, x):
        self.trailPoints.append(x)
        if len(self.trailPoints) > POINT_LIMIT:
            return self.trailPoints.popleft()
        else:
            return self.trailPoints[0]

def main():
    state = SystemState()
    motionThread = threading.Thread(target=motionTracking, args=(state,))
    logicThread = threading.Thread(target=changeData, args=(state,))
    motionThread.start()
    logicThread.start()

def motionTracking(state):
    threadStart = time.time();
    cap = cv2.VideoCapture(0)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # the HSV color values that are tracked
    lowH = 0
    highH = 40
    lowS = 61
    highS = 114
    lowV = 103
    highV = 166
    
    currentX = -1
    currentY = -1
    prevX = -1
    prevY = -1

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame,1) # flips along y-axis
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        thresh = cv2.inRange(hsv, (lowH, lowS, lowV), (highH, highS, highV))
        
        #morphological opening (removes small objects from the foreground)
        thresh = cv2.erode(thresh, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)))
        thresh = cv2.dilate(thresh, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)))
        
        momentData = cv2.moments(thresh)
        moment01 = momentData['m01']
        moment10 = momentData['m10']
        trackedArea = momentData['m00']

        if trackedArea > 10000:
            currentX = int(moment10 / trackedArea)
            currentY = int(moment01 / trackedArea)
        
        state.removedPoint = state.addPoint((currentX, currentY))
        prevX = currentX
        prevY = currentY

        trailEnd = state.trailPoints[0]
        dy = trailEnd[Y] - currentY
        dx = trailEnd[X] - currentX
        setDirection(dx, dy, state)
        
        cv2.waitKey(1)
        if time.time() - threadStart > 20: # quit with q
            break
        time.sleep(1/FPS)
    #clean-up after quitting
    cap.release()
    cv2.destroyAllWindows()
    print("Tracking thread complete")

def changeData(state):
    threadStart = time.time();
    while True:
        if state.currentPage == constants.Page.HOME:
            homeController.Control(state)
        elif state.currentPage == constants.Page.GAME:
            gameController.Control(state)
        elif state.currentPage == constants.Page.HISCORES:
            a = 0 # replace all a=0 lines with commented out controller lines
            #goto hiscoreController.Control(state)
        elif state.currentPage == constants.Page.HABITS:
            a = 0
            #goto habitsController.Control(state)
        elif state.currentPage == constants.Page.ENTERNAME:
            a = 0
            #goto nameController.Control(state)
        elif state.currentPage == constants.Page.LOGIN:
            a = 0
            #goto loginController.Control(state)
        
        cv2.waitKey(1)
        if time.time() - threadStart > 20: # quit with q
            break
        time.sleep(1/FPS)
    print("Logic thread complete")

def setDirection(dx, dy, state):
    global lastSwipe
    global direction
    global MIN_SWIPE
    global COOLDOWN
    length = math.hypot(dx, dy)
    if length > MIN_SWIPE and time.time() > state.lastSwipe + COOLDOWN: # direction is not modified if this is not satisfied
        state.lastSwipe = time.time()
        if dx != 0:
            slope = dy / dx
        else:
            slope = 50 # placeholder - any value >1 works
            
        if dy >= 0 and dx > 0:
            quadrant = 1
        elif dy >= 0 and dx <= 0:
            quadrant = 2
        elif dy < 0 and dx <= 0:
            quadrant = 3
        else:
            quadrant = 4
            
        if abs(slope) <= 1:
            if quadrant == 1 or quadrant == 4: # L/R might seem unintuitive, but recall screen is flipped along y-axis
                state.direction = constants.Direction.LEFT
            else:
                state.direction = constants.Direction.RIGHT
        else:
            if quadrant == 1 or quadrant == 2:
                state.direction = constants.Direction.UP
            else:
                state.direction = constants.Direction.DOWN



if __name__ == '__main__': main()
