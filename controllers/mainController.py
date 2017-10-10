import numpy as np
import cv2
import collections
import time
import math
import threading
import pickle
import os
from models import *
from views import *
from controllers import *
from enum import Enum
import constants
import startup

def main():
    directory = os.path.dirname(os.path.abspath(__file__)) + "\\users"
    state = systemState.SystemState()
    state.currentUser, state.userList, newUser = startup.getUser()
    if newUser:
        state.currentPage = constants.Page.ENTERNAME
    else:
        state.currentPage = constants.Page.HOME
    
    motionThread = threading.Thread(target=motionTracking, args=(state,))
    logicThread = threading.Thread(target=changeData, args=(state,))
    
    motionThread.start()
    logicThread.start()
    motionThread.join()
    logicThread.join()
    
    pickle.dump(state.currentUser, open("users\\" + state.currentUser.name, 'wb'))

def motionTracking(state):
    time.sleep(2)
    cap = cv2.VideoCapture(0)
    
    currentX = -1
    currentY = -1
    prevX = -1
    prevY = -1
    stopped = True

    while state.active:
        ret, frame = cap.read()
        frame = cv2.flip(frame,1) # flips along y-axis
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        thresh = cv2.inRange(hsv, (constants.LOW_H, constants.LOW_S, constants.LOW_V), (constants.HIGH_H, constants.HIGH_S, constants.HIGH_V))
        
        # removes small objects from foreground
        thresh = cv2.erode(thresh, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)))
        thresh = cv2.dilate(thresh, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)))
        
        momentData = cv2.moments(thresh)
        moment01 = momentData['m01']
        moment10 = momentData['m10']
        trackedArea = momentData['m00']

        if trackedArea > constants.MIN_SIZE:
            currentX = int(moment10 / trackedArea)
            currentY = int(moment01 / trackedArea)
        
        state.addPoint((currentX, currentY))
        
        if stopped:
            dy = currentY - prevY
            dx = currentX - prevX
            length = math.hypot(dx, dy)
            if length > 20: # 20 should be added to constants if this pans out
                stopped = False
        else: # if moving
            stillPoints = 0
            for id in range(len(state.trailPoints) - 1):
                dy = state.trailPoints[id][1] - state.trailPoints[id + 1][1]
                dx = state.trailPoints[id][0] - state.trailPoints[id + 1][0]
                length = math.hypot(dx, dy)
                if length < 20:
                    stillPoints += 1
            
            dy = state.motionStart[1] - currentY
            dx = state.motionStart[0] - currentX
            length = math.hypot(dx, dy)
            if length > constants.MIN_SWIPE:
                setDirection(dx, dy, state)
            if stillPoints >= 3: # 4 connections between 5 points, allow for one connection to be larger for stability
                stopped = True
                state.motionStart = (currentX, currentY)
                
        prevX = currentX
        prevY = currentY
        
        cv2.waitKey(1)
        time.sleep(1 / constants.FPS)
    
    cap.release()
    cv2.destroyAllWindows()

def changeData(state):
    threadStart = time.time()
    while state.active:
        if state.currentPage == constants.Page.HOME:
            homeController.Control(state)
        elif state.currentPage == constants.Page.GAME:
            gameController.Control(state)
        elif state.currentPage == constants.Page.HISCORE:
            hiscoreController.Control(state)
        elif state.currentPage == constants.Page.HABITS:
            habitsController.Control(state)
        elif state.currentPage == constants.Page.ENTERNAME:
            nameController.Control(state)
        elif state.currentPage == constants.Page.CALIBRATE:
            calibrateController.Control(state)
        elif state.currentPage == constants.Page.CONFIRM:
            confirmController.Control(state)
        
        cv2.waitKey(1)
        time.sleep(1 / constants.FPS)

def setDirection(dx, dy, state):
        
    if time.time() > state.lastSwipe + constants.COOLDOWN: # direction is not modified if this is not satisfied
        state.lastSwipe = time.time()
        if dx != 0:
            slope = dy / dx
        else:
            slope = 50 # any value >1 works
            
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
