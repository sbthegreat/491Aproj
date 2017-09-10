import numpy as np
import cv2
import constants
import numbers
import operator

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    cv2.putText(screen, "Home", constants.DOWN_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    
    scoreList = {}
    for storedUser in state.userList:
        scoreList[storedUser.name] = storedUser.highScore
    
    cv2.putText(screen, "High Scores:", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    scoreList = sorted(scoreList.items(), key = operator.itemgetter(1), reverse = True)
    counter = 1
    for pair in scoreList:
        cv2.putText(screen, str(counter) + ". " + pair[0] + ": " + str(pair[1]), (300, 100 + counter * 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
        counter += 1
    
    cv2.imshow('BrushSmart', screen)