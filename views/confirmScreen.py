import numpy as np
import cv2
import constants

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    
    cv2.putText(screen, "No", constants.UP_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Are you sure?", (300, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Yes", constants.DOWN_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.imshow('BrushSmart', screen)