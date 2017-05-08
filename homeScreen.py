import numpy as np
import cv2
import constants

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    cv2.putText(screen, "High Scores", constants.UP_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Habits", constants.LEFT_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Game", constants.RIGHT_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Quit", constants.DOWN_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    
    cv2.putText(screen, "Welcome, " + state.currentUser.name, (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    cv2.imshow('BrushSmart', screen)