import test as master
import numpy as np
import cv2
def Draw(state):
    screen = np.zeros((400,400,3), np.uint8)
    cv2.putText(screen, "its the game screen", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0))
    cv2.imshow('game', screen)