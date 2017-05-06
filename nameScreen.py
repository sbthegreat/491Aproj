import mainController as master
import numpy as np
import cv2
import constants

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    cv2.putText(screen, constants.ALPHABET[state.alphabetIndex - 1], (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, constants.ALPHABET[state.alphabetIndex], (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    cv2.putText(screen, constants.ALPHABET[(state.alphabetIndex + 1) % constants.ALPHA_SIZE], (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, state.currentUser.name, (200, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.imshow('BrushSmart', screen)