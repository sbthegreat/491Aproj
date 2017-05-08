import numpy as np
import cv2
import constants
import germ
import time

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    timeLeft = int(constants.GAME_LENGTH - (time.time() - state.gameStart))
    cv2.putText(screen, "Time: " + str(timeLeft), (550, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Score: " + str(state.gameScore), (550, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.circle(screen, (state.currentUser.gamePositionX, state.currentUser.gamePositionY), constants.GAME_SIZE, (255,255,255))
    
    mod = (time.time() - state.gameStart) % constants.SECTION_LENGTH
    if mod >= 0.2 and mod <= 2:
        cv2.ellipse(screen, (state.currentUser.gamePositionX, state.currentUser.gamePositionY), (constants.GAME_SIZE, constants.GAME_SIZE), 0, state.currentQuadrant, state.currentQuadrant + 90, (0, 0, 255), 2)
    
    for currentGerm in state.germList:
        cv2.circle(screen, (currentGerm.xPos, currentGerm.yPos), currentGerm.size, currentGerm.color, thickness=-1)
        
    for id in range(len(state.trailPoints) - 1):
        cv2.line(screen, state.trailPoints[id], state.trailPoints[id + 1], constants.TRAIL_COLOR)
    cv2.imshow('BrushSmart', screen)