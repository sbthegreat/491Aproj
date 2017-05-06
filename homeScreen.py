import mainController as master
import numpy as np
import cv2
import constants

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    cv2.putText(screen, "Welcome, " + state.currentUser.name, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    cv2.imshow('BrushSmart', screen)